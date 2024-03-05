from app.globals import page_setting

#ฟังชั่น ตรวจสอบว่าใช้งานเพียง 1 tab/server จริงหรือไม่
def set_only_one_tabs(page):
    if page_setting[page]['only_one_tab'] and page_setting[page]['current_usage']:
        return True
    page_setting[page]['current_usage'] = True
    return False