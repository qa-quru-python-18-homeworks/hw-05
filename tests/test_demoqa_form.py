import os.path

from selene import browser, be, have, command


def test_fill_in_form(maximize_browser):
    # Открыть страницу
    browser.open("https://demoqa.com/automation-practice-form")

    # Заполнить имя
    browser.element("#firstName").should(be.present).type("John").should(be.present.and_(have.value("John")))

    # Заполнить фамилию
    browser.element("#lastName").should(be.present).type("Doe").should(be.present.and_(have.value("Doe")))

    # Заполнить email
    browser.element("#userEmail").should(be.present).type("johndoe@example.com").should(
        be.present.and_(have.value("johndoe@example.com"))
    )

    # Выбрать пол (почему-то пришлось использовать js.click, если использовать click, то тест падает)
    browser.element("#gender-radio-1").should(be.present).perform(command.js.click).should(be.present.and_(be.selected))

    # Заполнить номер телефона
    browser.element("#userNumber").should(be.present).type("1234567890").should(
        be.present.and_(have.value("1234567890"))
    )

    # Заполнить дату рождения через календарь
    browser.element("#dateOfBirthInput").should(be.present).click()
    browser.element(".react-datepicker__month-select [value='0']").should(be.present).click()
    browser.element(".react-datepicker__year-select [value='1970']").should(be.present).click()
    browser.element(".react-datepicker__day.react-datepicker__day--001").should(be.present).click()
    browser.element("#dateOfBirthInput").should(have.value("01 Jan 1970"))

    # Заполнить предметы
    browser.element("#subjectsInput").should(be.present).type("Computer Science")
    browser.element("#react-select-2-option-0").should(be.present).click()
    browser.element(".subjects-auto-complete__multi-value__label").should(have.text("Computer Science"))

    # Выбрать все хобби (аналогично, как с полом, пришлось использовать js.click)
    browser.element("#hobbies-checkbox-1").should(be.present).perform(command.js.click).should(
        be.present.and_(be.selected)
    )
    browser.element("#hobbies-checkbox-2").should(be.present).perform(command.js.click).should(
        be.present.and_(be.selected)
    )
    browser.element("#hobbies-checkbox-3").should(be.present).perform(command.js.click).should(
        be.present.and_(be.selected)
    )

    # Загрузить картинку
    browser.element("#uploadPicture").should(be.present).type(
        os.path.join(os.path.dirname(__file__), "resources", "kitty.jpg")
    ).should(be.present.and_(have.value_containing("kitty.jpg")))

    # Заполнить адрес
    browser.element("#currentAddress").should(be.present).type("Connaught Place").should(
        be.present.and_(have.value("Connaught Place"))
    )

    # Выбрать штат...
    browser.element("#state").should(be.present).click()
    browser.element("#react-select-3-option-0").should(be.present).click()
    browser.element("#state").should(be.present.and_(have.text("NCR")))
    # ...и город
    browser.element("#city").should(be.present).click()
    browser.element("#react-select-4-option-0").should(be.present).click()
    browser.element("#city").should(be.present.and_(have.text("Delhi")))

    # Нажать кнопку Submit
    browser.element("#submit").should(be.present).click()

    # Проверить, что форма отправлена
    browser.element("#example-modal-sizes-title-lg").should(
        be.present.and_(have.text("Thanks for submitting the form"))
    )
