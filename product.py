class Product:
    def __init__(self, name, category="", price=0, currency=0, sku="", main_image="", additional_images=None,
                 description="", features=None, manufacturer="", warranty=""):
        self.name = name
        self.category = category
        self.price = price
        self.currency = currency
        self.sku = sku
        self.main_image = main_image
        self.additional_images = additional_images if additional_images is not None else []
        self.description = description
        self.features = features if features is not None else []
        self.manufacturer = manufacturer
        self.warranty = warranty
       

# דוגמה ליצירת מוצר חדש
product1 = Product(
    name="מכונת גילוח אלקטרית",
    category="טיפוח אישי",
    price=199.99,
    currency=0, # ביקשת שזה יהיה מספר שלם לכן זה מספרי
    sku="MG12345",
    main_image="product_images/mg12345_main.jpg",
    additional_images=["product_images/mg12345_1.jpg", "product_images/mg12345_2.jpg"],
    description="מכונת גילוח אלקטרית עם טכנולוגיה מתקדמת לתספוג חלק ומדויק.",
    features=["משטח גילוח גדול", "סוללה חזקה", "מנוע שקט"],
    manufacturer="סופרטק",
    warranty="שנתיים",
)


