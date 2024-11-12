async function fetchProducts() {
    const category = document.getElementById("category").value;  // Get selected category

    // Build query parameters for category filter
    let query = "/api/products?";
    if (category) {
        query += `category=${category}`;
    }

    console.log("Fetching data from:", query);  // Debugging log

    try {
        const response = await fetch(query);
        if (response.ok) {
            const products = await response.json();
            console.log("Products fetched:", products);  // Debugging log
            displayProducts(products);
        } else {
            console.error("Failed to fetch data:", response.status);
            document.getElementById("product-list").innerHTML = "Error loading products.";
        }
    } catch (error) {
        console.error("Error fetching products:", error);
        document.getElementById("product-list").innerHTML = "Error loading products.";
    }
}

function displayProducts(products) {
    const productList = document.getElementById("product-list");
    productList.innerHTML = ""; // Clear previous results

    // Check if there are products
    if (products.length === 0) {
        productList.innerHTML = "No products available.";
        return;
    }

    products.forEach(product => {
        const card = document.createElement("div");
        card.className = "product-card";

        const name = document.createElement("h3");
        name.innerText = product.name;

        const category = document.createElement("p");
        category.innerText = `Category: ${product.category}`;

        const price = document.createElement("div");
        price.className = "price";

        // Check for no discount
        if (!product.price.old_discount_percentage && !product.price.discount_percentage) {
            const originalPrice = document.createElement("span");
            originalPrice.className = "price-original";
            originalPrice.innerText = `Original Price: €${(product.price.original / 100).toFixed(2)}`;
            price.appendChild(originalPrice);
        } else {
            // If there's an old discount
            if (product.price.old_discount_percentage) {
                const oldDiscountText = document.createElement("span");
                oldDiscountText.className = "discount-line"; // Cross out old discount
                oldDiscountText.innerText = `${product.price.old_discount_percentage}% off (Old Discount)`;
                price.appendChild(oldDiscountText);
            }

            // New discounted price
            const finalPrice = document.createElement("span");
            finalPrice.className = "final-price";
            finalPrice.innerText = `New Price after discount: €${(product.price.final / 100).toFixed(2)}`;
            price.appendChild(finalPrice);
        }

        if (product.price.discount_percentage) {
            const discount = document.createElement("p");
            discount.className = "discount-text";
            discount.innerText = `Current Discount: ${product.price.discount_percentage}`;
            card.appendChild(discount);
        }

        card.appendChild(name);
        card.appendChild(category);
        card.appendChild(price);
        
        productList.appendChild(card);
    });
}

// Automatically load products on page load (optional)
document.addEventListener("DOMContentLoaded", () => {
    fetchProducts();
});
