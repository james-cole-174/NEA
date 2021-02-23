import mysqlmodule as msm

#msm.deleteRecord("products", "product_name", "Table")
msm.addRecordToTable("products", {"product_name":"Sofa", "unit_price":"59.99", "product_msrp":"59.99", "product_description":"It is a sofa. Seats at least 3 people. Cushiony foam, comfy.", "product_weight":"75"})