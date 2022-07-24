from store.admin import ProductAdmin
from store_custom.admin.util.TagInLine import TagInLine


class CustomProductAdmin(ProductAdmin):
    inlines = [TagInLine]
