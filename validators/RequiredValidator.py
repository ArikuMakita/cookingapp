from PyInquirer import Validator, ValidationError
class RequiredValidator(Validator):
    def validate(self, document):
        if not len(document.text):
            raise ValidationError(
                message='Поле не может быть пустым',
                cursor_position=len(document.text))
