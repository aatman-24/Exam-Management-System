from django.core.exceptions import ValidationError

class SlugCleanMixin:
    ''' Mixin class for slug cleaning method '''
    def clean_slug(self):       # both TagForm and StartupForm both contain this method.
        new_slug = (self.cleaned_data['slug'].lower())
        if new_slug == 'create' or new_slug == 'list' :
            raise ValidationError('Slug may not be "create".')
        return new_slug