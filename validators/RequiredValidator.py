from PyInquirer import Validator, ValidationError
class RequiredValidator(Validator):
    def validate(self, document):
        if not len(document.text):
            raise ValidationError(
                message='Пожалуйста введите название',
                cursor_position=len(document.text))
