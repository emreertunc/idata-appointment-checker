import string

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import schedule
import smtplib
from email.message import EmailMessage


def email_urgent(available_dates, branch_name):
    try:
        # E-posta içeriği
        msg = EmailMessage()
        msg.set_content(branch_name + ' en yakın tarihler: ' + available_dates)
        msg['Subject'] = branch_name + ' 2023 RANDEVU AÇILDI!!!!!!!!!!'
        msg['From'] = '******@gmail.com'
        msg['To'] = ['******@gmail.com', '******@gmail.com', '******@gmail.com', '******@gmail.com']

        # Gmail SMTP sunucusu ile bağlantı kur
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Gmail hesabınıza giriş yap
        server.login('******@gmail.com', '******')

        # E-postayı gönder
        server.send_message(msg)

        # Sunucu bağlantısını kapat
        server.quit()

    except:
        print("hata: mail gönderilemedi")


def email_general(available_dates, branch_name):
    try:
        # # E-posta içeriği
        # msg = EmailMessage()
        # msg.set_content(branch_name + ' en yakın tarihler: ' + available_dates)
        # msg['Subject'] = branch_name + ' 2023''te müsait tarih yok'
        # msg['From'] = '******@gmail.com'
        # msg['To'] = ['******@gmail.com', '******@gmail.com', '******@gmail.com']
        #
        # # Gmail SMTP sunucusu ile bağlantı kur
        # server = smtplib.SMTP('smtp.gmail.com', 587)
        # server.starttls()
        #
        # # Gmail hesabınıza giriş yap
        # server.login('******@gmail.com', '******')
        #
        # # E-postayı gönder
        # server.send_message(msg)
        #
        # # Sunucu bağlantısını kapat
        # server.quit()

        print('email not send for ' + branch_name)
    except:
        print("hata: mail gönderilemedi")


def check_idata_altunizade():
    driver = webdriver.Chrome()

    # Web sayfasını aç
    driver.get('https://deu-schengen.idata.com.tr/tr/appointment-form')

    wait = WebDriverWait(driver, 50)
    select_element = wait.until(EC.presence_of_element_located((By.ID, 'cookieJvns')))
    select_element.click()

    # "city" ID'sine sahip select elementini bulunana kadar bekle
    wait = WebDriverWait(driver, 50)
    select_element = wait.until(EC.presence_of_element_located((By.ID, 'city')))
    # value değeri "34" olan seçeneği seçin
    Select(select_element).select_by_value('34')

    select_element = wait.until(EC.presence_of_element_located((By.ID, 'office')))
    Select(select_element).select_by_value('8')

    select_element = wait.until(EC.presence_of_element_located((By.ID, 'totalPerson')))
    Select(select_element).select_by_value('1')

    # time.sleep(1)
    select_element = wait.until(EC.presence_of_element_located((By.ID, 'btnAppCountNext')))
    select_element.click()

    # SAYFA 2

    # Metin kutusunun yüklenmesini bekle
    text_field = wait.until(EC.presence_of_element_located((By.ID, 'name1')))
    # Metin kutusuna değer gönder
    text_field.send_keys("AHMET")

    text_field2 = wait.until(EC.presence_of_element_located((By.ID, 'surname1')))
    text_field2.send_keys("AHMETSOYAD")

    select_element = wait.until(EC.presence_of_element_located((By.ID, 'birthday1')))
    Select(select_element).select_by_value('10')

    select_element = wait.until(EC.presence_of_element_located((By.ID, 'birthmonth1')))
    Select(select_element).select_by_value('09')

    select_element = wait.until(EC.presence_of_element_located((By.ID, 'birthyear1')))
    Select(select_element).select_by_value('1999')

    text_field3 = wait.until(EC.presence_of_element_located((By.ID, 'passport1')))
    text_field3.send_keys("U111111111")

    text_field4 = wait.until(EC.presence_of_element_located((By.ID, 'phone1')))
    text_field4.send_keys("05336378339")

    text_field4 = wait.until(EC.presence_of_element_located((By.ID, 'email1')))
    text_field4.send_keys("abcabcabc@gmail.com")

    # time.sleep(1)
    select_element = wait.until(EC.presence_of_element_located((By.ID, 'btnAppPersonalNext')))
    select_element.click()

    # time.sleep(1)

    #### 3. SAYFA ONAY EKRANI
    select_element = wait.until(EC.presence_of_element_located((By.ID, 'btnAppPreviewNext')))
    select_element.click()
    # time.sleep(1)

    #### 4. SAYFA TARİH EKRANI

    date_field = wait.until(EC.presence_of_element_located((By.ID, 'flightDate')))
    date_field.click()

    while True:
        # "datepicker-switch" elementinin yüklenmesini bekleyin ve metnini alın
        datepicker_switch = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'datepicker-switch')))
        current_month_year = datepicker_switch.text

        # Eğer metin "February 2024" ise döngüden çık
        if current_month_year == "February 2024":
            break

        # "next" butonunun yüklenmesini bekleyin (th elementi için)
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'th.next')))
        time.sleep(1)

        # "next" butonuna tıklayın
        next_button.click()

    # "day" sınıfına ve içeriğe sahip olan hücreyi bekleyin
    day_to_click = wait.until(EC.presence_of_element_located((By.XPATH, "//td[@class='day' and text()='3']")))
    # Elemente tıklayın
    day_to_click.click()

    date_field2 = wait.until(EC.presence_of_element_located((By.ID, 'datepicker')))
    date_field2.click()
    # "day" sınıfına ve içeriğe sahip olan hücreyi bekleyin
    day_to_click2 = wait.until(EC.presence_of_element_located((By.XPATH, "//td[@class='today day']")))
    # Elemente tıklayın
    day_to_click2.click()

    #### AVAILABLE TARIHLERI ALMA

    wait = WebDriverWait(driver, 10)
    isDateAvailable: bool = False

    try:
        # 'availableDayInfo' ID'sine sahip div'in yüklenmesini bekle
        wait.until(EC.presence_of_element_located((By.ID, 'availableDayInfo')))
        time.sleep(3)
        # Div içindeki tarihleri al
        labels = driver.find_elements("xpath", "//div[@id='availableDayInfo']//label[@class='form-control']")
        dates = [label.text for label in labels]

        # Tarihleri birleştir ve bir değişkene at
        available_dates = ', '.join(dates)
        isDateAvailable = True

        print("Available dates:", available_dates)
    except TimeoutException:
        available_dates = "No available dates"
        isDateAvailable = False
        print(available_dates)

    # Tarayıcıyı kapat
    driver.quit()

    ### MAIL ATMA
    if isDateAvailable:
        if '2023' in available_dates:
            email_urgent(available_dates, 'ALTUNİZADE')
        else:
            email_general(available_dates, 'ALTUNİZADE')


def check_idata_gayrettepe():
    driver = webdriver.Chrome()

    # Web sayfasını aç
    driver.get('https://deu-schengen.idata.com.tr/tr/appointment-form')

    wait = WebDriverWait(driver, 50)
    select_element = wait.until(EC.presence_of_element_located((By.ID, 'cookieJvns')))
    select_element.click()

    # "city" ID'sine sahip select elementini bulunana kadar bekle
    wait = WebDriverWait(driver, 50)
    select_element = wait.until(EC.presence_of_element_located((By.ID, 'city')))
    # value değeri "34" olan seçeneği seçin
    Select(select_element).select_by_value('34')

    select_element = wait.until(EC.presence_of_element_located((By.ID, 'office')))
    Select(select_element).select_by_value('1')

    select_element = wait.until(EC.presence_of_element_located((By.ID, 'totalPerson')))
    Select(select_element).select_by_value('1')

    # time.sleep(1)
    select_element = wait.until(EC.presence_of_element_located((By.ID, 'btnAppCountNext')))
    select_element.click()

    # SAYFA 2

    # Metin kutusunun yüklenmesini bekle
    text_field = wait.until(EC.presence_of_element_located((By.ID, 'name1')))
    # Metin kutusuna değer gönder
    text_field.send_keys("AHMET")

    text_field2 = wait.until(EC.presence_of_element_located((By.ID, 'surname1')))
    text_field2.send_keys("AHMETSOYAD")

    select_element = wait.until(EC.presence_of_element_located((By.ID, 'birthday1')))
    Select(select_element).select_by_value('10')

    select_element = wait.until(EC.presence_of_element_located((By.ID, 'birthmonth1')))
    Select(select_element).select_by_value('09')

    select_element = wait.until(EC.presence_of_element_located((By.ID, 'birthyear1')))
    Select(select_element).select_by_value('1999')

    text_field3 = wait.until(EC.presence_of_element_located((By.ID, 'passport1')))
    text_field3.send_keys("U111111111")

    text_field4 = wait.until(EC.presence_of_element_located((By.ID, 'phone1')))
    text_field4.send_keys("05336378339")

    text_field4 = wait.until(EC.presence_of_element_located((By.ID, 'email1')))
    text_field4.send_keys("abcabcabc@gmail.com")

    # time.sleep(1)
    select_element = wait.until(EC.presence_of_element_located((By.ID, 'btnAppPersonalNext')))
    select_element.click()

    # time.sleep(1)

    #### 3. SAYFA ONAY EKRANI
    select_element = wait.until(EC.presence_of_element_located((By.ID, 'btnAppPreviewNext')))
    select_element.click()
    # time.sleep(1)

    #### 4. SAYFA TARİH EKRANI

    date_field = wait.until(EC.presence_of_element_located((By.ID, 'flightDate')))
    date_field.click()

    while True:
        # "datepicker-switch" elementinin yüklenmesini bekleyin ve metnini alın
        datepicker_switch = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'datepicker-switch')))
        current_month_year = datepicker_switch.text

        # Eğer metin "February 2024" ise döngüden çık
        if current_month_year == "February 2024":
            break

        # "next" butonunun yüklenmesini bekleyin (th elementi için)
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'th.next')))
        time.sleep(1)

        # "next" butonuna tıklayın
        next_button.click()

    # "day" sınıfına ve içeriğe sahip olan hücreyi bekleyin
    day_to_click = wait.until(EC.presence_of_element_located((By.XPATH, "//td[@class='day' and text()='3']")))
    # Elemente tıklayın
    day_to_click.click()

    date_field2 = wait.until(EC.presence_of_element_located((By.ID, 'datepicker')))
    date_field2.click()
    # "day" sınıfına ve içeriğe sahip olan hücreyi bekleyin
    day_to_click2 = wait.until(EC.presence_of_element_located((By.XPATH, "//td[@class='today day']")))
    # Elemente tıklayın
    day_to_click2.click()

    #### AVAILABLE TARIHLERI ALMA

    wait = WebDriverWait(driver, 10)
    isDateAvailable: bool = False

    try:
        # 'availableDayInfo' ID'sine sahip div'in yüklenmesini bekle
        wait.until(EC.presence_of_element_located((By.ID, 'availableDayInfo')))
        time.sleep(3)
        # Div içindeki tarihleri al
        labels = driver.find_elements("xpath", "//div[@id='availableDayInfo']//label[@class='form-control']")
        dates = [label.text for label in labels]

        # Tarihleri birleştir ve bir değişkene at
        available_dates = ', '.join(dates)
        isDateAvailable = True

        print("Available dates:", available_dates)
    except TimeoutException:
        available_dates = "No available dates"
        isDateAvailable = False
        print(available_dates)

    # Tarayıcıyı kapat
    driver.quit()

    ### MAIL ATMA
    if isDateAvailable:
        if '2023' in available_dates:
            email_urgent(available_dates, 'GAYRETTEPE')
        else:
            email_general(available_dates, 'GAYRETTEPE')


def check_idata_bursa():
    driver = webdriver.Chrome()

    # Web sayfasını aç
    driver.get('https://deu-schengen.idata.com.tr/tr/appointment-form')

    wait = WebDriverWait(driver, 50)
    select_element = wait.until(EC.presence_of_element_located((By.ID, 'cookieJvns')))
    select_element.click()

    # "city" ID'sine sahip select elementini bulunana kadar bekle
    wait = WebDriverWait(driver, 50)
    select_element = wait.until(EC.presence_of_element_located((By.ID, 'city')))
    # value değeri "34" olan seçeneği seçin
    Select(select_element).select_by_value('34')

    select_element = wait.until(EC.presence_of_element_located((By.ID, 'office')))
    Select(select_element).select_by_value('5')

    select_element = wait.until(EC.presence_of_element_located((By.ID, 'totalPerson')))
    Select(select_element).select_by_value('1')

    # time.sleep(1)
    select_element = wait.until(EC.presence_of_element_located((By.ID, 'btnAppCountNext')))
    select_element.click()

    # SAYFA 2

    # Metin kutusunun yüklenmesini bekle
    text_field = wait.until(EC.presence_of_element_located((By.ID, 'name1')))
    # Metin kutusuna değer gönder
    text_field.send_keys("AHMET")

    text_field2 = wait.until(EC.presence_of_element_located((By.ID, 'surname1')))
    text_field2.send_keys("AHMETSOYAD")

    select_element = wait.until(EC.presence_of_element_located((By.ID, 'birthday1')))
    Select(select_element).select_by_value('10')

    select_element = wait.until(EC.presence_of_element_located((By.ID, 'birthmonth1')))
    Select(select_element).select_by_value('09')

    select_element = wait.until(EC.presence_of_element_located((By.ID, 'birthyear1')))
    Select(select_element).select_by_value('1999')

    text_field3 = wait.until(EC.presence_of_element_located((By.ID, 'passport1')))
    text_field3.send_keys("U111111111")

    text_field4 = wait.until(EC.presence_of_element_located((By.ID, 'phone1')))
    text_field4.send_keys("05336378339")

    text_field4 = wait.until(EC.presence_of_element_located((By.ID, 'email1')))
    text_field4.send_keys("abcabcabc@gmail.com")

    # time.sleep(1)
    select_element = wait.until(EC.presence_of_element_located((By.ID, 'btnAppPersonalNext')))
    select_element.click()

    # time.sleep(1)

    #### 3. SAYFA ONAY EKRANI
    select_element = wait.until(EC.presence_of_element_located((By.ID, 'btnAppPreviewNext')))
    select_element.click()
    # time.sleep(1)

    #### 4. SAYFA TARİH EKRANI

    date_field = wait.until(EC.presence_of_element_located((By.ID, 'flightDate')))
    date_field.click()

    while True:
        # "datepicker-switch" elementinin yüklenmesini bekleyin ve metnini alın
        datepicker_switch = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'datepicker-switch')))
        current_month_year = datepicker_switch.text

        # Eğer metin "February 2024" ise döngüden çık
        if current_month_year == "February 2024":
            break

        # "next" butonunun yüklenmesini bekleyin (th elementi için)
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'th.next')))
        time.sleep(1)

        # "next" butonuna tıklayın
        next_button.click()

    # "day" sınıfına ve içeriğe sahip olan hücreyi bekleyin
    day_to_click = wait.until(EC.presence_of_element_located((By.XPATH, "//td[@class='day' and text()='3']")))
    # Elemente tıklayın
    day_to_click.click()

    date_field2 = wait.until(EC.presence_of_element_located((By.ID, 'datepicker')))
    date_field2.click()
    # "day" sınıfına ve içeriğe sahip olan hücreyi bekleyin
    day_to_click2 = wait.until(EC.presence_of_element_located((By.XPATH, "//td[@class='today day']")))
    # Elemente tıklayın
    day_to_click2.click()

    #### AVAILABLE TARIHLERI ALMA

    wait = WebDriverWait(driver, 10)
    isDateAvailable: bool = False

    try:
        # 'availableDayInfo' ID'sine sahip div'in yüklenmesini bekle
        wait.until(EC.presence_of_element_located((By.ID, 'availableDayInfo')))
        time.sleep(3)
        # Div içindeki tarihleri al
        labels = driver.find_elements("xpath", "//div[@id='availableDayInfo']//label[@class='form-control']")
        dates = [label.text for label in labels]

        # Tarihleri birleştir ve bir değişkene at
        available_dates = ', '.join(dates)
        isDateAvailable = True

        print("Available dates:", available_dates)
    except TimeoutException:
        available_dates = "No available dates"
        isDateAvailable = False
        print(available_dates)

    # Tarayıcıyı kapat
    driver.quit()

    ### MAIL ATMA
    if isDateAvailable:
        if '2023' in available_dates:
            email_urgent(available_dates, 'BURSA')
        else:
            email_general(available_dates, 'BURSA')


schedule.every(2).minutes.do(check_idata_altunizade)
schedule.every(2).minutes.do(check_idata_gayrettepe)
schedule.every(2).minutes.do(check_idata_bursa)

while True:
    schedule.run_pending()
    time.sleep(1)
