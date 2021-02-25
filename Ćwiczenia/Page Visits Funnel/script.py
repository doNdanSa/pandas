import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
parse_dates=[1])
cart = pd.read_csv('cart.csv',
parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
parse_dates=[1])

print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

v_cart = pd.merge(visits, cart, how='left')
v_cart_len = len(v_cart)
#print(v_cart_len)

v_cart_null = v_cart[v_cart.cart_time.isnull()]
#print(len(v_cart_null))
v_cart_null_len = len(v_cart_null)

print(float(v_cart_null_len)/v_cart_len)

######################################

c_cart = pd.merge(cart, checkout, how='left')
c_cart_len = len(c_cart)
#print(c_cart_len)
# print(c_cart)

c_cart_null = c_cart[c_cart.checkout_time.isnull()]
#print(len(c_cart_null))
c_cart_null_len = len(c_cart_null)

print(float(c_cart_null_len)/c_cart_len)

checkout_purchase = pd.merge(checkout, purchase, how='left')
checkout_purchase_rows = len(checkout_purchase)
checkout_purchase_null = len(checkout_purchase[checkout_purchase.purchase_time.isnull()])
print(float(checkout_purchase_null)/ checkout_purchase_rows)

all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')
#print(all_data.head())

all_data['time_to_purchase'] = \
all_data.purchase_time - \
all_data.visit_time

print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())

