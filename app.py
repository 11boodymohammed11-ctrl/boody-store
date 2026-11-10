from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# قائمة المنتجات المطورة مع الأقسام، الألوان، والمخزون
PRODUCTS = [
    {
        "id": 1,
        "name": "هوودي أوفر سايز",
        "category": "sweatshirts",
        "price": 450,
        "image": "sweatshirt1.jpg",
        "description": "خامة مولتون ثقيلة مبطنة من الداخل لتدفئة فائقة في الشتاء.",
        "sizes": ["M", "L", "XL"],
        "colors": ["أسود كلاسيك", "رمادي فاتح", "كحلي داكن"],
        "stock": 5
    },
    {
        "id": 2,
        "name": "بنطال كارجو كاجوال",
        "category": "pants",
        "price": 380,
        "image": "pants1.jpg",
        "description": "تصميم كارجو عملي بجيوب متعددة، قطن مرن مريح جداً للحركة.",
        "sizes": ["30", "32", "34", "36"],
        "colors": ["زيتوني عسكري", "بيج رملي", "أسود فحمى"],
        "stock": 2 # تنبيه باقي قطعتين فقط
    },
    {
        "id": 3,
        "name": "كوتشي سنيكرز رياضي",
        "category": "shoes",
        "price": 620,
        "image": "shoes1.jpg",
        "description": "نعل مريح وممتاز للمشي الطويل، تصميم عصري يتناسب مع كل الستايلات.",
        "sizes": ["41", "42", "43", "44"],
        "colors": ["أبيض في أسود", "أبيض بالكامل"],
        "stock": 8
    }
]

@app.route('/')
def index():
    return render_template('index.html', products=PRODUCTS)

@app.route('/api/cart/calculate', methods=['POST'])
def calculate_cart():
    data = request.json or {}
    items = data.get('items', [])
    
    subtotal = sum(item['price'] * item['quantity'] for item in items)
    total_items = sum(item['quantity'] for item in items)
    
    # تطبيق خصم 15% لو اشتري قطعتين أو أكثر
    discount = 0
    if total_items >= 2:
        discount = subtotal * 0.15
        
    total = subtotal - discount
    
    return jsonify({
        'subtotal': subtotal,
        'discount': discount,
        'total': total,
        'total_items': total_items,
        'eligible_for_discount': total_items >= 2
    })

if __name__ == '__main__':
    app.run(debug=True)