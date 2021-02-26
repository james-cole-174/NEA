import mysqlmodule as msm

product_dictionary = {
    "product_name":"Chair",
    "unit_price":"59.00",
    "product_msrp":"59.00",
    "product_description":"Its a chair",
    "product_weight":"15"
}

customer_dictionary = {
    "first_name":"James",
    "last_name":"Cole",
    "title":"Mr",
    "email":"james@test.com",
    "phone":"07788999239"
}

#msm.deleteRecord("products", "product_name", "Chair")
#msm.addRecordToTable("products", product_dictionary)
msm.addRecordToTable("customers", customer_dictionary)
print(msm.getAllTableDict("customers"))