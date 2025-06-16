import React from 'react';
import { Star, ShoppingCart, Eye } from 'lucide-react';
import { Product } from '../../types';
import { useCart } from '../../contexts/CartContext';

interface ProductCardProps {
  product: Product;
  onViewDetails: (product: Product) => void;
}

export default function ProductCard({ product, onViewDetails }: ProductCardProps) {
  const { addItem } = useCart();

  const handleAddToCart = (e: React.MouseEvent) => {
    e.stopPropagation();
    if (product.inStock) {
      addItem(product);
    }
  };

  const handleViewDetails = () => {
    onViewDetails(product);
  };

  return (
    <div 
      className="bg-white rounded-xl shadow-lg p-6 max-w-sm mx-auto flex flex-col"
      data-testid="product-card"
      data-product-id={product.id}
      data-product-name={product.name}
      onClick={handleViewDetails}
    >
      {/* Image */}
      <div className="mb-4">
        <img
          src={product.image}
          alt={product.name}
          className="w-full h-48 object-cover rounded-lg"
          data-testid="product-image"
        />
      </div>

      {/* Content */}
      <div className="flex-1 flex flex-col">
        {/* Title */}
        <h3 
          className="text-xl font-semibold text-gray-900 mb-2 line-clamp-2"
          data-testid="product-title"
        >
          {product.name}
        </h3>

        {/* Description */}
        <p 
          className="text-sm text-gray-600 mb-4 line-clamp-3"
          data-testid="product-description"
        >
          {product.description}
        </p>

        {/* Rating */}
        <div className="flex items-center gap-2 mb-4">
          <div className="flex gap-1" data-testid="product-rating">
            {/* Stars */}
            {[...Array(5)].map((_, i) => (
              <Star
                key={i}
                className={`h-4 w-4 ${
                  i < Math.floor(product.rating)
                    ? 'text-yellow-400 fill-current'
                    : 'text-gray-300'
                }`}
              />
            ))}
          </div>
          <span 
            className="text-sm text-gray-500 font-medium"
            data-testid="product-rating-text"
          >
            {product.rating} ({product.reviews})
          </span>
        </div>

        {/* Price & Button */}
        <div className="flex items-center justify-between mt-auto pt-2">
          <div className="flex flex-col">
            <span 
              className="text-2xl font-bold text-gray-900"
              data-testid="product-price"
            >
              ${product.price.toFixed(2)}
            </span>
            {product.originalPrice && (
              <span 
                className="text-sm text-gray-500 line-through"
                data-testid="product-original-price"
              >
                ${product.originalPrice.toFixed(2)}
              </span>
            )}
          </div>

          <button
            onClick={handleAddToCart}
            disabled={!product.inStock}
            className={`flex items-center space-x-1 px-4 py-2.5 rounded-lg text-sm font-medium transition-all duration-200 ${
              product.inStock
                ? 'bg-blue-600 text-white hover:bg-blue-700 hover:shadow-lg'
                : 'bg-gray-300 text-gray-500 cursor-not-allowed'
            }`}
            title={product.inStock ? 'Add to Cart' : 'Out of Stock'}
            data-testid="add-to-cart-button"
            data-product-id={product.id}
            data-stock-status={product.inStock ? 'in-stock' : 'out-of-stock'}
          >
            <ShoppingCart className="w-4 h-4" />
            <span className="text-xs">
              {product.inStock ? 'Add to Cart' : 'Out of Stock'}
            </span>
          </button>
        </div>
      </div>
    </div>
  );
}