import customtkinter
import pytz
import json
import os
import base64
import requests
import subprocess
import threading
import sys
import sqlite3
import platform

from datetime import datetime, date, timedelta
from time import sleep
from getpass import getuser
from pathlib import Path

from Crypto.Cipher import AES

vn_timezone = pytz.timezone("Asia/Ho_Chi_Minh")


class IMessageXAPI:
    DOMAIN_NAME = "https://imessagex.bunnydream.site"
    # DOMAIN_NAME = "http://127.0.0.1:8000"
    headers = {"Accept": "application/json"}

    def update_serial_number_named(self, serial_number_named):
        url = f"{self.DOMAIN_NAME}/api/macbook-serial/"

        serial_number = helper.get_serial_number()

        data = {"serial_number": serial_number, "serial_named": serial_number_named}

        # response = requests.patch(f"{url}{serial_number}", headers=headers, json=data)
        response = requests.post(url, headers=self.headers, json=data)
        if response.status_code != 201:
            response = requests.patch(
                f"{url}{serial_number}/", headers=self.headers, json=data
            )

    def get_and_save_scripts(self, data: dict):
        url = f"{self.DOMAIN_NAME}/api/get/"
        response = requests.post(url, headers=self.headers, json=data)
        if response.status_code == 200:
            folder = os.path.join(CONFIG.APP_FOLDER, ".com")
            Path(folder).mkdir(parents=True, exist_ok=True)
            json_response = response.json()
            for key in ["1", "2", "3"]:
                value = json_response.get(key)
                fpath = os.path.join(folder, f"{key}")
                if not Path(fpath).is_file():
                    with open(fpath, "w") as f:
                        f.write(value)

    def get_aes_key_and_validation_string(self, license_key: str) -> str:
        aes_key = "0"
        message = CONFIG.SERVER_ERROR_TEXT
        try:
            url = f"{self.DOMAIN_NAME}/api/check/"
            data = {
                "license_key": license_key,
                "serial_number": helper.get_serial_number(),
            }

            response = requests.post(url, headers=self.headers, json=data)

            response_json = response.json()
            message = response_json.get("message")

            if response.status_code == 200:
                self.get_and_save_scripts(data)
                aes_key = response_json.get("data")
            else:
                aes_key = "1"

        except:
            pass

        return [aes_key, message]

    def get_phone_statistics(self, license_key: str = ""):
        res = {}
        try:
            url = f"{self.DOMAIN_NAME}/api/stats/"
            data = {
                "serial_number": helper.get_serial_number(),
            }
            response = requests.post(url, headers=self.headers, json=data)
            if response.status_code == 200:
                res = response.json()

            try:
                url = f"{self.DOMAIN_NAME}/api/vip-stats/"
                data["license_key"] = license_key
                response = requests.post(url, headers=self.headers, json=data)
                if response.status_code == 200:
                    res["vip"] = response.json()
            except:
                pass
        except:
            pass

        return res

    def update_node_sent(self, serial_number, date, sent, tag):
        url = f"{self.DOMAIN_NAME}/api/node/"
        data = {
            "serial_number": serial_number,
            "date": date,
            "sent": sent,
            "tag": tag,
        }
        response = requests.post(url, headers=self.headers, json=data)

    def post_phone(self, number, date, serial_number, tag, is_read: bool = False):
        url = f"{self.DOMAIN_NAME}/api/phone/"
        data = {
            "number": number,
            "date": date,
            "serial_number": serial_number,
            "tag": tag,
            "is_read": is_read,
        }
        response = requests.post(url, headers=self.headers, json=data)

    def get_file_by_serial(
        self, license_key, serial_number, user_id, is_getting_vip: bool = False
    ):
        url = f"{self.DOMAIN_NAME}/api/file/"
        if is_getting_vip:
            url = f"{self.DOMAIN_NAME}/api/vip-file/"
        data = {
            "license_key": license_key,
            "serial_number": serial_number,
            "user_id": user_id,
        }
        response = requests.post(url, headers=self.headers, json=data)

        return response.json().get("message")


iMessageXAPI = IMessageXAPI()


class Config:
    APP_FOLDER = f"/Users/{getuser()}/.imessagex"
    Path(APP_FOLDER).mkdir(parents=True, exist_ok=True)

    APP_JSON_FOLDER = os.path.join(APP_FOLDER, "json")
    Path(APP_JSON_FOLDER).mkdir(parents=True, exist_ok=True)

    PHONE_PREFIX = "+84"

    APP_FOLDER_NAMED_FILE = os.path.join(APP_FOLDER, ".named")

    DATABASE_NAME = f"{APP_FOLDER}/imessagex.db"
    # DATABASE_NAME = f"/Users/{getuser()}/Library/Messages/imessagex.db"

    LICENSE_TABLE = "license"

    INSERT = {
        LICENSE_TABLE: ["key"],
    }

    LICENSE_INVALID_TEXT = "License is invalid!"
    SERVER_ERROR_TEXT = (
        "Can not connect to the server. Please contact the administrators."
    )
    GET_IMESSAGE_NUMBERS_HELP_TEXT = """Step 1. Go to telegram, search for "imessagex_bot"
Step 2. Press Start in the private chatbox with imessagex_bot.
Step 3. Enter command below in the private chatbox with imessagex_bot
                /get_id
Step 4. Copy the User ID and paste to the Telegram ID input field below.
Step 5. Press Get file to get the file contains imessage numbers in the private chat with imessage_bot.


WARNING: Please don't spam this Get file option. Otherwise your license might be banned.
"""


CONFIG = Config()


class Database:
    def __init__(self):
        conn = self.get_conn()
        cursor = conn.cursor()
        # Create a table
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS license
                        (id INTEGER PRIMARY KEY, key TEXT)"""
        )
        conn.commit()
        conn.close()
        self.select_or_insert(table=CONFIG.LICENSE_TABLE, condition="id=1", data=("",))

    def get_conn(self):
        try:
            conn = sqlite3.connect(CONFIG.DATABASE_NAME)
            return conn
        except Exception as e:
            print(f"Error connecting to Sqlite database: {e}")
            sys.exit(1)

    def select_with(self, query: str) -> list:
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute(query)
        res = cur.fetchall()
        cur.close()
        conn.close()

        return res

    def select_all_from(self, table: str, condition: str = "1=1", cols: str = "*"):
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute(f"SELECT {cols} FROM {table} WHERE {condition}")
        res = cur.fetchall()
        cur.close()
        conn.close()

        return res

    def insert_into(self, table: str, data: tuple = None, is_bulk: bool = False):
        conn = self.get_conn()
        cur = conn.cursor()
        id = 0

        columns = f"({', '.join(CONFIG.INSERT[table])})"
        values = f"({', '.join(['?'] * len(CONFIG.INSERT[table]))})"
        query = f"INSERT INTO {table} {columns} VALUES {values}"
        if is_bulk:
            cur.executemany(query, data)
        else:
            cur.execute(query, data)
            id = cur.lastrowid

        conn.commit()
        cur.close()
        conn.close()
        return id

    def update_table(
        self, table: str, set_cond: str, where_cond: str, data: tuple = ()
    ):
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute(f"UPDATE {table} set {set_cond} WHERE {where_cond}", data)
        conn.commit()
        cur.close()
        conn.close()

    def delete_from(self, table: str = "", condition: str = "1=1"):
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM {table} WHERE {condition}")
        conn.commit()
        cur.close()
        conn.close()

    def select_or_insert(self, table: str, condition: str, data: tuple):
        res = self.select_all_from(table=table, condition=condition)
        if not res:
            self.insert_into(table, data)
            res = self.select_all_from(table, condition=condition)
        return res


database = Database()


def deliver_attachment(attachment, contact, aes_key):
    fname = "2"
    mac_version = platform.mac_ver()[0]
    if int(float(mac_version.split(".")[0])) > 11:
        fname = "3"
    apple_script_file_path = build_apple_script_file_path(fname, aes_key)

    cmd = f'osascript {apple_script_file_path} "{contact}" "{attachment}"'

    os.system(cmd)
    os.system(f"rm -rf {apple_script_file_path}")


def deliver_text(text, contact, aes_key):
    apple_script_file_path = build_apple_script_file_path("1", aes_key)

    cmd = f'osascript {apple_script_file_path} "{contact}" "{text}"'

    os.system(cmd)
    os.system(f"rm -rf {apple_script_file_path}")


def build_apple_script_file_path(filename, aes_key):
    file_folder = os.path.join(CONFIG.APP_FOLDER, ".com")
    file_path = os.path.join(file_folder, filename)
    with open(file_path, "r") as f:
        data = f.read().strip("\n")

    ciphertext, tag, nonce = data.split("$$")
    aes_key = base64.b64decode(aes_key)

    cipher = AES.new(aes_key, AES.MODE_EAX, base64.b64decode(nonce))
    data = cipher.decrypt_and_verify(
        base64.b64decode(ciphertext), base64.b64decode(tag)
    )
    send_file_path = os.path.join(file_folder, f"{filename}.applescript")
    with open(send_file_path, "w") as send_file:
        print(data.decode(), file=send_file)

    return send_file_path


class Helper:
    def get_serial_number(self):
        command = "system_profiler SPHardwareDataType | awk '/Serial/ {print $4}'"
        serial_number = subprocess.check_output(command, shell=True).decode().strip()
        return serial_number

    def get_serial_number_named(self):
        serial_number_named = ""
        if Path(CONFIG.APP_FOLDER_NAMED_FILE).is_file():
            with open(CONFIG.APP_FOLDER_NAMED_FILE, "r") as f:
                serial_number_named = f.read().strip("\n")
        return serial_number_named

    def clear_folder(self):
        kfile = os.path.join(CONFIG.APP_FOLDER, ".k")
        cmd = f"rm -rf {kfile}"
        os.system(cmd)

        folder = os.path.join(CONFIG.APP_FOLDER, ".com")
        cmd = f"rm -rf {folder}"
        os.system(cmd)

    def get_license(self):
        try:
            license = database.select_all_from(table=CONFIG.LICENSE_TABLE)
            return license[0][-1]
        except:
            return ""

    def update_license(self, new_license_key: str):
        try:
            database.update_table(
                table=CONFIG.LICENSE_TABLE,
                set_cond=f"key='{new_license_key}'",
                where_cond="id=1",
            )
            return "OK"
        except:
            return "Error"

    def update_serial_number_named(self, new_serial_number_named: str):
        try:
            with open(CONFIG.APP_FOLDER_NAMED_FILE, "w") as f:
                f.write(new_serial_number_named)

            iMessageXAPI.update_serial_number_named(new_serial_number_named)
        except:
            return "Error"

    def get_file_content(self, file_path: str):
        with open(file_path) as f:
            lines = f.readlines()

        return [x.strip("\n") for x in lines]


helper = Helper()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("iMessageX")
        self.minsize(width=960, height=526)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand("tk::mac::Quit", self.on_closing)

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(
            self.navigation_frame,
            text="  iMessageX",
            compound="left",
            font=customtkinter.CTkFont(size=15, weight="bold"),
        )
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Home",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
            command=self.home_button_event,
        )
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.stats_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Statistics",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
            command=self.stats_frame_button_event,
        )
        self.stats_button.grid(row=2, column=0, sticky="ew")

        self.license_frame_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="License",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
            command=self.license_frame_button_event,
        )
        self.license_frame_button.grid(row=3, column=0, sticky="ew")

        self.get_imessage_numbers_frame_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Get iMessage Numbers",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
            command=self.get_imessage_numbers_frame_button_event,
        )
        self.get_imessage_numbers_frame_button.grid(row=4, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(
            self.navigation_frame,
            values=["System", "Light", "Dark"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        self.home_frame.grid_columnconfigure(1, weight=1)
        self.home_frame.grid_rowconfigure(7, weight=1)

        # Tag
        self.home_frame_tag_label = customtkinter.CTkLabel(
            self.home_frame, text="                          Tag"
        )
        self.home_frame_tag_label.grid(
            row=0, column=0, padx=20, pady=(10, 0), sticky="w"
        )
        self.home_frame_tag_input = customtkinter.CTkEntry(self.home_frame)
        self.home_frame_tag_input.grid(
            row=0, column=1, padx=20, pady=(10, 0), sticky="ew"
        )
        self.home_frame_tag_input.insert(0, "")

        self.home_frame_textbox = customtkinter.CTkTextbox(self.home_frame)
        self.home_frame_textbox.grid(row=1, columnspan=2, padx=20, pady=10, sticky="ew")
        self.home_frame_textbox.insert("1.0", "Text to send")

        # Delay time between sending to messages
        self.home_frame_delay_time_label = customtkinter.CTkLabel(
            self.home_frame, text="Time between 2 messages"
        )
        self.home_frame_delay_time_label.grid(
            row=3, column=0, padx=20, pady=10, sticky="w"
        )
        self.home_frame_delay_time_input = customtkinter.CTkEntry(
            self.home_frame,
            validate="key",
            validatecommand=(
                self.home_frame.register(self.validate_sleep_time),
                "%P",
            ),
        )
        self.home_frame_delay_time_input.grid(
            row=3, column=1, padx=20, pady=10, sticky="ew"
        )
        self.home_frame_delay_time_input.insert(0, "2")

        # Attachment
        # self.home_frame_is_send_attachment = customtkinter.CTkCheckBox(
        #     master=self.home_frame, text="Send attachment?"
        # )
        # self.home_frame_is_send_attachment.grid(
        #     row=3, column=0, pady=10, padx=20, sticky="w"
        # )

        self.home_frame_attachment_button = customtkinter.CTkButton(
            self.home_frame,
            text="Attachment",
            command=self.attachment_button_handle_folder,
        )
        self.home_frame_attachment_button.grid(
            row=4, column=0, padx=20, pady=10, sticky="w"
        )

        self.home_frame_attachment_input = customtkinter.CTkEntry(self.home_frame)
        self.home_frame_attachment_input.grid(
            row=4, column=1, padx=20, pady=10, sticky="ew"
        )
        self.home_frame_attachment_input.insert(0, "")
        self.home_frame_attachment_input.configure(state="readonly")

        # Contacts file

        self.home_frame_contact_button = customtkinter.CTkButton(
            self.home_frame,
            text="Contacts file",
            command=self.contact_button_handle_folder,
        )
        self.home_frame_contact_button.grid(
            row=5, column=0, padx=20, pady=10, sticky="w"
        )

        self.home_frame_contact_input = customtkinter.CTkEntry(self.home_frame)
        self.home_frame_contact_input.grid(
            row=5, column=1, padx=20, pady=10, sticky="ew"
        )
        self.home_frame_contact_input.insert(0, "")
        self.home_frame_contact_input.configure(state="readonly")

        # WARING
        self.home_frame_warning_label = customtkinter.CTkLabel(self.home_frame, text="")
        self.home_frame_warning_label.grid(
            row=6, columnspan=2, padx=20, pady=10, sticky="ew"
        )

        # Send/Stop button
        self.home_frame_sending_state = False
        self.home_frame_send_button = customtkinter.CTkButton(
            self.home_frame, text="Send", command=self.home_frame_send_button_handle
        )
        self.home_frame_send_button.grid(
            row=7, columnspan=2, padx=20, pady=(10, 0), sticky="ew"
        )

        # create statistics frame
        self.stats_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        self.stats_frame.grid_columnconfigure(1, weight=1)

        self.stats_frame_today_sent_label = customtkinter.CTkLabel(
            self.stats_frame, text="Today sent"
        )
        self.stats_frame_today_sent_label.grid(row=0, column=0, padx=20, pady=(40, 10))

        self.stats_frame_today_sent_input = customtkinter.CTkEntry(self.stats_frame)
        self.stats_frame_today_sent_input.grid(
            row=0, column=1, padx=20, pady=(40, 10), sticky="ew"
        )

        self.stats_frame_today_imessage_label = customtkinter.CTkLabel(
            self.stats_frame, text="Today iMessage"
        )
        self.stats_frame_today_imessage_label.grid(row=1, column=0, padx=20, pady=10)

        self.stats_frame_today_imessage_input = customtkinter.CTkEntry(self.stats_frame)
        self.stats_frame_today_imessage_input.grid(
            row=1, column=1, padx=20, pady=10, sticky="ew"
        )

        self.stats_frame_month_sent_label = customtkinter.CTkLabel(
            self.stats_frame, text="Month sent"
        )
        self.stats_frame_month_sent_label.grid(row=2, column=0, padx=20, pady=10)

        self.stats_frame_month_sent_input = customtkinter.CTkEntry(self.stats_frame)
        self.stats_frame_month_sent_input.grid(
            row=2, column=1, padx=20, pady=10, sticky="ew"
        )

        self.stats_frame_month_imessage_label = customtkinter.CTkLabel(
            self.stats_frame, text="Month iMessage"
        )
        self.stats_frame_month_imessage_label.grid(row=3, column=0, padx=20, pady=10)

        self.stats_frame_month_imessage_input = customtkinter.CTkEntry(self.stats_frame)
        self.stats_frame_month_imessage_input.grid(
            row=3, column=1, padx=20, pady=10, sticky="ew"
        )

        self.stats_frame_all_sent_label = customtkinter.CTkLabel(
            self.stats_frame, text="All sent"
        )
        self.stats_frame_all_sent_label.grid(row=4, column=0, padx=20, pady=10)

        self.stats_frame_all_sent_input = customtkinter.CTkEntry(self.stats_frame)
        self.stats_frame_all_sent_input.grid(
            row=4, column=1, padx=20, pady=10, sticky="ew"
        )

        self.stats_frame_all_imessage_label = customtkinter.CTkLabel(
            self.stats_frame, text="All iMessage"
        )
        self.stats_frame_all_imessage_label.grid(row=5, column=0, padx=20, pady=10)

        self.stats_frame_all_imessage_input = customtkinter.CTkEntry(self.stats_frame)
        self.stats_frame_all_imessage_input.grid(
            row=5, column=1, padx=20, pady=10, sticky="ew"
        )

        self.stats_frame_vip_stats_label = customtkinter.CTkLabel(
            self.stats_frame, text="VIP"
        )
        self.stats_frame_vip_stats_label.grid(
            row=6, columnspan=2, padx=20, pady=(10, 0), sticky="ew"
        )

        self.stats_frame_vip_stats_textbox = customtkinter.CTkTextbox(self.stats_frame)
        self.stats_frame_vip_stats_textbox.grid(
            row=7, columnspan=2, padx=20, pady=10, sticky="ew"
        )

        # create license frame
        self.license_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )

        self.license_frame.grid_columnconfigure(1, weight=1)
        self.license_frame.grid_rowconfigure(4, weight=1)

        self.license_frame_serial_number_label = customtkinter.CTkLabel(
            self.license_frame, text="Serial Number"
        )
        self.license_frame_serial_number_label.grid(
            row=0, column=0, padx=20, pady=(40, 10)
        )

        self.license_frame_serial_number = customtkinter.CTkEntry(self.license_frame)
        self.license_frame_serial_number.grid(
            row=0, column=1, padx=20, pady=(40, 10), sticky="ew"
        )
        self.license_frame_serial_number.insert(0, helper.get_serial_number())
        self.license_frame_serial_number.configure(state="readonly")

        ###
        self.license_frame_serial_number_named_label = customtkinter.CTkLabel(
            self.license_frame, text="Named"
        )
        self.license_frame_serial_number_named_label.grid(
            row=1, column=0, padx=20, pady=10
        )

        self.license_frame_serial_number_named = customtkinter.CTkEntry(
            self.license_frame
        )
        self.license_frame_serial_number_named.grid(
            row=1, column=1, padx=20, pady=10, sticky="ew"
        )
        self.license_frame_serial_number_named.insert(
            0, helper.get_serial_number_named()
        )
        self.license_frame_serial_number_named.configure(state="readonly")
        ###

        self.license_frame_license_label = customtkinter.CTkLabel(
            self.license_frame, text="License"
        )
        self.license_frame_license_label.grid(row=2, column=0, padx=20, pady=10)

        self.license_frame_license_input = customtkinter.CTkEntry(self.license_frame)
        self.license_frame_license_input.grid(
            row=2, column=1, padx=20, pady=10, sticky="ew"
        )
        self.license_key = helper.get_license()
        self.license_frame_license_input.insert(0, self.license_key)
        self.license_frame_license_input.configure(state="readonly")
        # self.license_frame_license_input.configure(state="normal")

        self.license_frame_license_key_valid_text = customtkinter.CTkLabel(
            self.license_frame, text="Checking..."
        )
        self.license_frame_license_key_valid_text.grid(
            row=3, columnspan=2, padx=20, pady=10
        )

        self.license_frame_edit_and_save_button_state = "Edit"
        self.license_frame_edit_and_save_button = customtkinter.CTkButton(
            self.license_frame,
            text="Edit",
            command=self.license_frame_edit_and_save_button_event,
        )
        self.license_frame_edit_and_save_button.grid(
            row=4, columnspan=2, padx=20, pady=20, sticky="ew"
        )

        # creat get imessages numbers frame
        self.get_imessage_numbers_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        self.get_imessage_numbers_frame.grid_columnconfigure(1, weight=1)
        self.get_imessage_numbers_frame.grid_rowconfigure(8, weight=1)

        self.get_imessage_numbers_frame_textbox_label = customtkinter.CTkLabel(
            self.get_imessage_numbers_frame, text="How to use?"
        )
        self.get_imessage_numbers_frame_textbox_label.grid(
            row=0, columnspan=2, padx=20, pady=(10, 0), sticky="ew"
        )

        self.get_imessage_numbers_frame_textbox = customtkinter.CTkTextbox(
            self.get_imessage_numbers_frame
        )
        self.get_imessage_numbers_frame_textbox.grid(
            row=1, columnspan=2, padx=20, pady=10, sticky="ew"
        )
        self.get_imessage_numbers_frame_textbox.insert(
            "1.0", CONFIG.GET_IMESSAGE_NUMBERS_HELP_TEXT
        )
        self.get_imessage_numbers_frame_textbox.configure(state="disabled")

        self.get_imessage_numbers_frame_telegram_id_label = customtkinter.CTkLabel(
            self.get_imessage_numbers_frame, text="Telegram ID"
        )
        self.get_imessage_numbers_frame_telegram_id_label.grid(
            row=3, column=0, padx=20, pady=10, sticky="w"
        )
        telegram_id_path = os.path.join(CONFIG.APP_FOLDER, "telegram")
        if Path(telegram_id_path).is_file():
            telegram_id = open(telegram_id_path).read().strip("\n")
        else:
            telegram_id = ""
        self.get_imessage_numbers_frame_telegram_id_input = customtkinter.CTkEntry(
            self.get_imessage_numbers_frame
        )
        self.get_imessage_numbers_frame_telegram_id_input.grid(
            row=3, column=1, padx=20, pady=10, sticky="ew"
        )
        self.get_imessage_numbers_frame_telegram_id_input.insert("0", telegram_id)

        self.get_imessage_numbers_frame_result_label = customtkinter.CTkLabel(
            self.get_imessage_numbers_frame, text=""
        )
        self.get_imessage_numbers_frame_result_label.grid(
            row=4, columnspan=2, padx=20, pady=10, sticky="ew"
        )

        self.get_imessage_numbers_frame_get_button = customtkinter.CTkButton(
            self.get_imessage_numbers_frame,
            text="Get file",
            command=self.get_imessage_numbers_frame_get_button_handle,
        )
        self.get_imessage_numbers_frame_get_button.grid(
            row=5, columnspan=2, padx=20, pady=(10, 0), sticky="ew"
        )

        self.get_imessage_numbers_frame_spacer_label = customtkinter.CTkLabel(
            self.get_imessage_numbers_frame, text=""
        )
        self.get_imessage_numbers_frame_spacer_label.grid(
            row=6, columnspan=2, padx=20, pady=10, sticky="ew"
        )

        self.get_imessage_numbers_frame_get_vip_button = customtkinter.CTkButton(
            self.get_imessage_numbers_frame,
            text="Get VIP file",
            command=self.get_imessage_numbers_frame_get_vip_button_handle,
        )

        # select default frame
        self.select_frame_by_name("home")
        self.is_checking_license_key = True
        threading.Thread(target=self.check_license_key).start()
        self.is_running_update_statistics = True
        threading.Thread(target=self.update_statistics).start()

    def validate_sleep_time(self, text: str):
        if text.endswith("."):
            text = text + "0"
        try:
            value = float(text)
            if value >= 0:
                return True
        except:
            return False

    def get_and_set_phones_statics(self):
        self.phone_statistics = iMessageXAPI.get_phone_statistics(self.license_key)

        stats_pattern = {
            "today_sent": self.stats_frame_today_sent_input,
            "today_imessage": self.stats_frame_today_imessage_input,
            "month_sent": self.stats_frame_month_sent_input,
            "month_imessage": self.stats_frame_month_imessage_input,
            "all_sent": self.stats_frame_all_sent_input,
            "all_imessage": self.stats_frame_all_imessage_input,
        }
        for key, entry_input in stats_pattern.items():
            entry_input.configure(state="normal")
            entry_input.delete(0, customtkinter.END)
            entry_input.insert(0, self.phone_statistics.get(key, "-"))
            entry_input.configure(state="readonly")

        self.vip_phone_statistics = self.phone_statistics.get("vip", "")
        if not self.vip_phone_statistics:
            self.stats_frame_vip_stats_label.grid_forget()
            self.stats_frame_vip_stats_textbox.grid_forget()
            self.get_imessage_numbers_frame_get_vip_button.grid_forget()
        else:
            self.stats_frame_vip_stats_label.grid(
                row=6, columnspan=2, padx=20, pady=(10, 0), sticky="ew"
            )

            self.stats_frame_vip_stats_textbox.grid(
                row=7, columnspan=2, padx=20, pady=10, sticky="ew"
            )

            self.get_imessage_numbers_frame_get_vip_button.grid(
                row=7, columnspan=2, padx=20, pady=(10, 0), sticky="ew"
            )

            self.stats_frame_vip_stats_textbox.configure(state="normal")
            self.stats_frame_vip_stats_textbox.delete("1.0", customtkinter.END)
            self.stats_frame_vip_stats_textbox.insert(
                "1.0", self.get_vip_stats(self.vip_phone_statistics)
            )
            self.stats_frame_vip_stats_textbox.configure(state="disabled")

    def get_vip_stats(self, vip_stats: dict) -> str:
        res = ""
        for serial_number, serial_stats in vip_stats.items():
            today_imessage = serial_stats.get("today_imessage", "-")
            today_sent = serial_stats.get("today_sent", "-")
            month_imessage = serial_stats.get("month_imessage", "-")
            month_sent = serial_stats.get("month_sent", "-")
            all_imessage = serial_stats.get("all_imessage", "-")
            all_sent = serial_stats.get("all_sent", "-")

            res += f"Serial number: {serial_number}\n\tToday:\t{today_imessage}/{today_sent}\tiMessages/Sent\n\tMonth:\t{month_imessage}/{month_sent}\tiMessages/Sent\n\tAll:\t{all_imessage}/{all_sent}\tiMessages/Sent\n\n"

        return res

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(
            fg_color=("gray75", "gray25") if name == "home" else "transparent"
        )
        self.stats_button.configure(
            fg_color=("gray75", "gray25") if name == "stats_frame" else "transparent"
        )
        self.license_frame_button.configure(
            fg_color=("gray75", "gray25") if name == "license_frame" else "transparent"
        )
        self.get_imessage_numbers_frame_button.configure(
            fg_color=("gray75", "gray25")
            if name == "get_imessage_numbers_frame"
            else "transparent"
        )

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "stats_frame":
            self.stats_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.stats_frame.grid_forget()
        if name == "license_frame":
            self.license_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.license_frame.grid_forget()
        if name == "get_imessage_numbers_frame":
            self.get_imessage_numbers_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.get_imessage_numbers_frame.grid_forget()

    def license_frame_edit_and_save_button_event(self):
        if self.license_frame_edit_and_save_button_state == "Edit":
            self.license_frame_license_input.focus()
            self.license_frame_edit_and_save_button_state = "Save"
            self.license_frame_edit_and_save_button.configure(text="Save")
            self.license_frame_license_input.configure(state="normal")
            self.license_frame_serial_number_named.configure(state="normal")
        else:
            self.license_frame_edit_and_save_button_state = "Edit"

            self.license_key = self.license_frame_license_input.get()
            self.serial_number_named = self.license_frame_serial_number_named.get()
            helper.update_license(new_license_key=self.license_key)
            helper.update_serial_number_named(
                new_serial_number_named=self.serial_number_named
            )
            self.license_frame_license_key_valid_text.configure(text="Checking...")

            self.license_frame_edit_and_save_button.configure(text="Edit")
            self.license_frame_license_input.configure(state="readonly")
            self.license_frame_serial_number_named.configure(state="readonly")

    def home_button_event(self):
        self.select_frame_by_name("home")

    def stats_frame_button_event(self):
        self.select_frame_by_name("stats_frame")

    def license_frame_button_event(self):
        self.select_frame_by_name("license_frame")

    def get_imessage_numbers_frame_button_event(self):
        self.select_frame_by_name("get_imessage_numbers_frame")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def attachment_button_handle_folder(self):
        folder = customtkinter.filedialog.askopenfilename()
        if not folder:
            return

        self.home_frame_attachment_input.configure(state="normal")
        self.home_frame_attachment_input.delete(0, customtkinter.END)
        self.home_frame_attachment_input.insert(0, folder)
        self.home_frame_attachment_input.configure(state="readonly")

    def contact_button_handle_folder(self):
        folder = customtkinter.filedialog.askopenfilename()
        if not folder:
            return
        self.home_frame_contact_input.configure(state="normal")
        self.home_frame_contact_input.delete(0, customtkinter.END)
        self.home_frame_contact_input.insert(0, folder)
        self.home_frame_contact_input.configure(state="readonly")

    def send_text_and_attachment(self):
        tag = self.home_frame_tag_input.get()
        tag = tag if tag else "Unknown"
        text_message = self.home_frame_textbox.get("1.0", "end-1c")
        delay_time = self.home_frame_delay_time_input.get()
        attachment = self.home_frame_attachment_input.get()

        contacts_path = self.home_frame_contact_input.get()
        if contacts_path:
            contacts = helper.get_file_content(file_path=contacts_path)

            for contact in contacts:
                contact = contact.strip("\n").strip()

                kpath = os.path.join(CONFIG.APP_FOLDER, ".k")
                if not Path(kpath).is_file():
                    continue
                else:
                    with open(kpath, "r") as f:
                        aes_key = f.read().strip("\n")

                if not self.home_frame_sending_state:
                    break

                if text_message:
                    deliver_text(text_message, contact, aes_key)
                    sleep(float(delay_time))

                if attachment:
                    deliver_attachment(attachment, contact, aes_key)
                    sleep(float(delay_time))

                self.write_tag_sent_number(tag=tag, contact=contact)

        self.stop_sending_text_and_attachment()
        self.home_frame_sending_state = False

    def get_tag_today_file_path(self, tag: str) -> str:
        date_time = datetime.now(vn_timezone)
        date_str = date_time.strftime("%Y-%m-%d")

        key = f"{tag}_{date_str}"
        tag_today_file_path = os.path.join(CONFIG.APP_JSON_FOLDER, f"{key}.json")

        return tag_today_file_path

    def read_json_file(
        self,
        json_path,
        is_default_list: bool = True,
    ) -> list | dict:
        if Path(json_path).is_file():
            json_file_content = json.loads(open(json_path, "r").read())
        else:
            json_file_content = [] if is_default_list else {}

        # print(json_file_content)
        return json_file_content

    def write_json_file(self, write_obj, json_path):
        if not write_obj:
            return
        with open(json_path, "w") as f:
            f.write(json.dumps(write_obj, indent=4))

    def write_tag_sent_number(self, tag, contact: str):
        tag_today_file_path = self.get_tag_today_file_path(tag=tag)
        tag_sent_numbers = self.read_json_file(json_path=tag_today_file_path)
        if contact.startswith("0"):
            contact = CONFIG.PHONE_PREFIX + contact[1:]
        tag_sent_numbers.append(contact)
        self.write_json_file(write_obj=tag_sent_numbers, json_path=tag_today_file_path)

    def stop_sending_text_and_attachment(self):
        self.home_frame_textbox.configure(state="normal")
        self.home_frame_delay_time_input.configure(state="normal")
        self.home_frame_attachment_button.configure(state="normal")
        self.home_frame_contact_button.configure(state="normal")
        self.home_frame_send_button.configure(text="Send")

    def home_frame_send_button_handle(self):
        self.home_frame_sending_state = not self.home_frame_sending_state
        if self.home_frame_sending_state:
            self.home_frame_textbox.configure(state="disabled")
            self.home_frame_delay_time_input.configure(state="readonly")
            self.home_frame_attachment_button.configure(state="disabled")
            self.home_frame_contact_button.configure(state="disabled")
            self.home_frame_send_button.configure(text="Stop")
            threading.Thread(target=self.send_text_and_attachment).start()

        else:
            self.stop_sending_text_and_attachment()

    def get_imessage_numbers_file_and_set_result(
        self, telegram_user_id, is_getting_vip: bool = False
    ):
        self.get_imessage_numbers_frame_result_label.configure(text="Getting file...")
        response_text = iMessageXAPI.get_file_by_serial(
            self.license_key,
            helper.get_serial_number(),
            telegram_user_id,
            is_getting_vip=is_getting_vip,
        )
        self.get_imessage_numbers_frame_result_label.configure(text=response_text)

    def get_imessage_numbers_frame_get_button_handle(self):
        telegram_user_id = self.get_imessage_numbers_frame_telegram_id_input.get()
        telegram_id_path = os.path.join(CONFIG.APP_FOLDER, "telegram")
        with open(telegram_id_path, "w") as f:
            f.write(telegram_user_id)

        threading.Thread(
            target=self.get_imessage_numbers_file_and_set_result,
            args=(telegram_user_id,),
        ).start()

    def get_imessage_numbers_frame_get_vip_button_handle(self):
        telegram_user_id = self.get_imessage_numbers_frame_telegram_id_input.get()
        telegram_id_path = os.path.join(CONFIG.APP_FOLDER, "telegram")
        with open(telegram_id_path, "w") as f:
            f.write(telegram_user_id)

        threading.Thread(
            target=self.get_imessage_numbers_file_and_set_result,
            args=(telegram_user_id, True),
        ).start()

    def on_closing(self, event=0):
        self.is_running_update_statistics = False
        self.home_frame_sending_state = False
        self.is_checking_license_key = False
        helper.clear_folder()
        sys.exit(1)
        for _ in range(20):
            if threading.active_count() > 1:
                sleep(1)
                continue

        if threading.active_count() <= 1:
            self.destroy()
        else:
            sys.exit(1)

    def update_statistics(self):
        while True:
            try:
                if not self.is_running_update_statistics:
                    return

                tag = self.home_frame_tag_input.get()
                tag = tag if tag else "Unknown"

                tag_today_file_path = self.get_tag_today_file_path(tag=tag)
                tag_sent_numbers = self.read_json_file(json_path=tag_today_file_path)
                # print(tag_sent_numbers)

                serial_number = helper.get_serial_number()
                conn = sqlite3.connect(f"/Users/{getuser()}/Library/Messages/chat.db")
                # conn = sqlite3.connect("/Users/devil/AnhCuong/imessagex/chat.db")

                c = conn.cursor()

                date_time = datetime.now(vn_timezone)
                today = date_time.date()
                today_start = today.strftime("%Y-%m-%d") + " 00:00:00"
                today_end = today.strftime("%Y-%m-%d") + " 23:59:59"
                today_start = datetime.strptime(today_start, "%Y-%m-%d %H:%M:%S")
                today_end = datetime.strptime(today_end, "%Y-%m-%d %H:%M:%S")

                today_start_imessage = (
                    today_start.timestamp() - 978307200
                ) * 1000000000
                today_end_imessage = (today_end.timestamp() - 978307200) * 1000000000

                iMessageXAPI.update_node_sent(
                    serial_number=serial_number,
                    date=today.strftime("%Y-%m-%d"),
                    sent=len(tag_sent_numbers),
                    tag=tag,
                )

                is_sent_numbers = []
                c.execute(
                    f"""SELECT handle_id FROM message WHERE (is_sent=1 or error=0)
                            AND is_from_me=1 AND date>={today_start_imessage} AND date<={today_end_imessage}"""
                )

                handle_ids = [handle_id[0] for handle_id in c.fetchall()]

                handle_ids = list(set(handle_ids))

                for handle_id in handle_ids:
                    if not self.is_running_update_statistics:
                        return

                    c.execute(
                        f"SELECT id FROM handle WHERE service='iMessage' and ROWID='{handle_id}'"
                    )
                    phone_number = c.fetchone()
                    if phone_number:
                        is_sent_numbers.append(phone_number[0])

                # print("is_sent_numbers")
                # print(is_sent_numbers)

                is_read_numbers = []
                c.execute(
                    f"""SELECT handle_id FROM message WHERE is_read=1
                            AND is_from_me=1 AND date>={today_start_imessage} AND date<={today_end_imessage}"""
                )

                handle_ids = [handle_id[0] for handle_id in c.fetchall()]

                handle_ids = list(set(handle_ids))

                for handle_id in handle_ids:
                    if not self.is_running_update_statistics:
                        return

                    c.execute(
                        f"SELECT id FROM handle WHERE service='iMessage' and ROWID='{handle_id}'"
                    )
                    phone_number = c.fetchone()
                    if phone_number:
                        is_read_numbers.append(phone_number[0])

                # print("is_read_numbers")
                # print(is_read_numbers)

                for is_read_number in is_read_numbers:
                    if str(
                        is_read_number
                    ) not in tag_sent_numbers or self.is_updated_statistics_for_number(
                        number=is_read_number,
                        date_str=today.strftime("%Y-%m-%d"),
                        tag=tag,
                        is_read=True,
                    ):
                        continue

                    iMessageXAPI.post_phone(
                        number=is_read_number,
                        date=today.strftime("%Y-%m-%d"),
                        serial_number=serial_number,
                        tag=tag,
                        is_read=True,
                    )

                for is_sent_number in is_sent_numbers:
                    if str(is_sent_number) not in tag_sent_numbers or (
                        is_sent_number in is_read_numbers
                        or self.is_updated_statistics_for_number(
                            number=is_sent_number,
                            date_str=today.strftime("%Y-%m-%d"),
                            tag=tag,
                        )
                    ):
                        continue

                    iMessageXAPI.post_phone(
                        number=is_sent_number,
                        date=today.strftime("%Y-%m-%d"),
                        serial_number=serial_number,
                        tag=tag,
                    )

                self.get_and_set_phones_statics()

            except Exception as e:
                print(e)

            for _ in range(600):
                if not self.is_running_update_statistics:
                    return

                sleep(0.1)

    def is_updated_statistics_for_number(
        self, number, date_str, tag, is_read: bool = False
    ) -> bool:
        updated_path = os.path.join(
            CONFIG.APP_JSON_FOLDER, f"updated_{tag}_{date_str}.json"
        )
        updated_list = self.read_json_file(json_path=updated_path, is_default_list=True)

        key = f"{number}_{'1' if is_read else '0'}"
        if key in updated_list:
            return True

        updated_list.append(key)

        self.write_json_file(write_obj=updated_list, json_path=updated_path)
        return False

    def check_license_key(self):
        while True:
            try:
                (
                    aes_key,
                    license_validation_string,
                ) = iMessageXAPI.get_aes_key_and_validation_string(self.license_key)

                if aes_key == "0" or aes_key == "1":
                    self.warning_text = (
                        CONFIG.LICENSE_INVALID_TEXT
                        if aes_key == "1"
                        else CONFIG.SERVER_ERROR_TEXT
                    )

                    helper.clear_folder()
                else:
                    self.warning_text = ""
                    kfile = os.path.join(CONFIG.APP_FOLDER, ".k")
                    if not Path(kfile).is_file():
                        with open(kfile, "w") as f:
                            f.write(aes_key)

                self.home_frame_warning_label.configure(text=self.warning_text)

                self.license_frame_license_key_valid_text.configure(
                    text=license_validation_string
                )

            except Exception as e:
                print(e)

            for _ in range(100):
                if not self.is_checking_license_key:
                    return

                sleep(0.1)


if __name__ == "__main__":
    try:
        app = App()
        app.mainloop()
    except Exception as e:
        print(e)
        sleep(1000)
