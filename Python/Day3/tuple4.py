subscribers = {
    "saniya@gmail.com",
    "ayman@gmail.com",
    "zara@gmail.com",
    "Shifa@gmail.com"
}

customers = {
    "ayman@gmail.com",
    "shifa@gmail.com",
    "ayesha@gmail.com",
    "fatima@gmail.com"
}

subscribers_wo_purchase = subscribers - customers
customers_wo_subscription = customers - subscribers

print("Subscribers without purchase:", subscribers_wo_purchase)
print("Customers without subscription:", customers_wo_subscription)
