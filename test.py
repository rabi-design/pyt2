import PySimpleGUI as sg

# 画面レイアウトを指定
layout = [
    [sg.Text('日給計算アプリ')],
    [sg.Text('開始時間', size = (15, 1)), sg.InputText('09:00')],
    [sg.Text('終了時間', size = (15, 1)), sg.InputText('17:00')],
    [sg.Text('休憩時間', size = (15, 1)), sg.InputText('1:00')],
    [sg.Text('時給', size = (15, 1)), sg.InputText('1100')],
    [sg.Submit(button_text = '計算')]]


# ウィンドウを表示する関数
def show_window():
    win = sg.Window('日給計算', layout)
    # イベントループ
    while True:
        event, values = win.read()
        if event is None:
            break
        if event == '計算':  # --- (*1)
            calc_payment(values)


# 時給計算 --- (*2)
def calc_payment(values):
    # フィールドから値を取得
    start_t = timestr_to_min(values[0])
    end_t = timestr_to_min(values[1])
    rest_t = timestr_to_min(values[2])
    jikyu = values[3]
    # 取得した値から時給を計算
    m = (end_t - start_t - rest_t)
    val = int((m / 60) * float(jikyu))
    # 結果を表示
    sg.popup("結果:" + str(val) + "円")


# HH:MMの形式を分に変換 --- (*3)
def timestr_to_min(hm):
    h, m = hm.split(":")  # 時と分に分ける
    return int(h) * 60 + int(m)


show_window()
