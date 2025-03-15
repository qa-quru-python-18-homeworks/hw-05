import os.path
from selene import browser, be, have, command


def test_fill_in_form(maximize_browser):
    # Открыть страницу
    browser.open("https://demoqa.com/automation-practice-form")

    # Заполнить имя
    browser.element("#firstName").type("John").should(have.value("John"))

    # Заполнить фамилию
    browser.element("#lastName").type("Doe").should(have.value("Doe"))

    # Заполнить email
    browser.element("#userEmail").type("johndoe@example.com").should(have.value("johndoe@example.com"))

    # Выбрать пол (почему-то пришлось использовать js.click, если использовать click, то тест падает)
    browser.element("#gender-radio-1").perform(command.js.click).should(be.selected)

    # Заполнить номер телефона
    browser.element("#userNumber").type("1234567890").should(have.value("1234567890"))

    # Заполнить дату рождения через календарь
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select [value='0']").click()
    browser.element(".react-datepicker__year-select [value='1970']").click()
    browser.element(".react-datepicker__day.react-datepicker__day--001").click()
    browser.element("#dateOfBirthInput").should(have.value("01 Jan 1970"))

    # Заполнить предметы
    browser.element("#subjectsInput").type("Computer Science")
    browser.element("#react-select-2-option-0").click()
    browser.element(".subjects-auto-complete__multi-value__label").should(have.text("Computer Science"))

    # Выбрать все хобби (аналогично, как с полом, пришлось использовать js.click)
    browser.element("#hobbies-checkbox-1").perform(command.js.click).should(be.selected)
    browser.element("#hobbies-checkbox-2").perform(command.js.click).should(be.selected)
    browser.element("#hobbies-checkbox-3").perform(command.js.click).should(be.selected)

    # Загрузить картинку
    browser.element("#uploadPicture").type(
        os.path.join(os.path.dirname(__file__), "resources", "kitty.jpg")
    ).should(have.value_containing("kitty.jpg"))

    # Заполнить адрес
    browser.element("#currentAddress").type("Connaught Place").should(have.value("Connaught Place"))

    # Выбрать штат...
    browser.element("#state").click()
    browser.element("#react-select-3-option-0").click()
    browser.element("#state").should(have.text("NCR"))
    # ...и город
    browser.element("#city").click()
    browser.element("#react-select-4-option-0").click()
    browser.element("#city").should(have.text("Delhi"))

    # Нажать кнопку Submit
    browser.element("#submit").click()

    # Проверить, что форма отправлена
    browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))

    # Проверить, что данные в таблице совпадают с введенными
    browser.all("tbody tr td:nth-child(2)").should(have.texts([
        "John Doe", "johndoe@example.com", "Male", "1234567890", "01 January,1970", "Computer Science",
        "Sports, Reading, Music", "kitty.jpg", "Connaught Place", "NCR Delhi"
    ]))
