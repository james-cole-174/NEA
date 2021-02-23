import mysqlmodule as msm

product_dictionary = {
    "product_name":"Sony 55 Inch KD55A8BU Smart 4K UHD HDR OLED Android TV",
    "unit_price":"1299.00",
    "product_msrp":"1299.00",
    "product_description":"The A8 OLED uses Sony best ever picture processor to create stunningly realistic images, and working with Pixel Contrast Booster, colour and contrast is enhanced for extra depth and texture. Sound and picture are in perfect harmony with Acoustic Surface Audio. BRAVIA OLED for incredible contrast, true-to-life colour, a blur-free image and an exceptionally wide viewing angle. The Sony BRAVIA KD55A8 includes the same flagship processor that drives our 8K TVs, analysing the individual objects in each picture and boosting the colour, contrast and clarity.",
    "product_weight":"18.6"
}

msm.deleteRecord("products", "product_name", "Table")
msm.deleteRecord("products", "product_name", "Chair")
msm.deleteRecord("products", "product_name", "Sofa")
msm.deleteRecord("products", "product_name", "Bed")
msm.deleteRecord("products", "product_name", "TV")
#msm.addRecordToTable("products", product_dictionary)