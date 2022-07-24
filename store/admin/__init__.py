# Register your models here.

from store.admin.util.InventoryFilter import InventoryFilter
from store.admin.CollectionAdmin import CollectionAdmin
from store.admin.CustomerAdmin import CustomerAdmin
from store.admin.ProductAdmin import ProductAdmin
from store.admin.OrderAdmin import OrderAdmin

# Override the base query set used to render the list page
# If we want to show the number of products in each collection in the collection.
