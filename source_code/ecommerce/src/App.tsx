import React, { useState, useMemo } from 'react';
import { AuthProvider } from './contexts/AuthContext';
import { CartProvider } from './contexts/CartContext';
import Header from './components/Layout/Header';
import ProductGrid from './components/Products/ProductGrid';
import ProductFilters from './components/Products/ProductFilters';
import ProductDetail from './components/Products/ProductDetail';
import Cart from './components/Cart/Cart';
import AuthModal from './components/Auth/AuthModal';
import ProfileModal from './components/Profile/ProfileModal';
import CheckoutModal from './components/Checkout/CheckoutModal';
import { products, categories } from './data/products';
import { Product } from './types';

function App() {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('All');
  const [priceRange, setPriceRange] = useState<[number, number]>([0, 1500]);
  const [selectedProduct, setSelectedProduct] = useState<Product | null>(null);
  const [isCartOpen, setIsCartOpen] = useState(false);
  const [isAuthDialogOpen, setAuthDialogOpen] = useState(false);
  const [isProfileModalOpen, setIsProfileModalOpen] = useState(false);
  const [isCheckoutModalOpen, setIsCheckoutModalOpen] = useState(false);
  const [isFiltersOpen, setIsFiltersOpen] = useState(false);

  const maxPrice = Math.max(...products.map(p => p.price));

  const filteredProducts = useMemo(() => {
    return products.filter(product => {
      const matchesSearch = product.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
                          product.description.toLowerCase().includes(searchQuery.toLowerCase());
      const matchesCategory = selectedCategory === 'All' || product.category === selectedCategory;
      const matchesPrice = product.price >= priceRange[0] && product.price <= priceRange[1];
      
      return matchesSearch && matchesCategory && matchesPrice;
    });
  }, [searchQuery, selectedCategory, priceRange]);

  const handleClearFilters = () => {
    setSelectedCategory('All');
    setPriceRange([0, maxPrice]);
    setSearchQuery('');
  };

  const handleCheckout = () => {
    setIsCartOpen(false);
    setIsCheckoutModalOpen(true);
  };

  return (
    <AuthProvider>
      <CartProvider>
        <div className="min-h-screen bg-gray-50">
          <Header
            onSearchChange={setSearchQuery}
            onCartClick={() => setIsCartOpen(true)}
            onAuthClick={() => setAuthDialogOpen(true)}
            onProfileClick={() => setIsProfileModalOpen(true)}
            isAuthDialogOpen={isAuthDialogOpen}
          />

          <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <div className="flex flex-col lg:flex-row gap-8">
              {/* Filters Sidebar */}
              <div className="lg:w-64 flex-shrink-0">
                <ProductFilters
                  categories={categories}
                  selectedCategory={selectedCategory}
                  priceRange={priceRange}
                  maxPrice={maxPrice}
                  onCategoryChange={setSelectedCategory}
                  onPriceRangeChange={setPriceRange}
                  onClearFilters={handleClearFilters}
                  isOpen={isFiltersOpen}
                  onToggle={() => setIsFiltersOpen(!isFiltersOpen)}
                />
              </div>

              {/* Products Grid */}
              <div className="flex-1">
                <div className="mb-6">
                  <div className="flex items-center justify-between">
                    {/* US-014: Display selected category */}
                    <h2 className="text-2xl font-bold text-gray-900">
                      {selectedCategory === 'All' ? 'All Products' : selectedCategory}
                    </h2>
                    <p className="text-gray-600">
                      {filteredProducts.length} product{filteredProducts.length !== 1 ? 's' : ''} found
                    </p>
                  </div>
                  {searchQuery && (
                    <p className="text-sm text-gray-600 mt-2">
                      Showing results for "{searchQuery}"
                    </p>
                  )}
                </div>

                <ProductGrid
                  products={filteredProducts}
                  onViewDetails={setSelectedProduct}
                />
              </div>
            </div>
          </main>

          {selectedProduct && (
            <ProductDetail
              product={selectedProduct}
              onClose={() => setSelectedProduct(null)}
            />
          )}

          <Cart
            isOpen={isCartOpen}
            onClose={() => setIsCartOpen(false)}
            onCheckout={handleCheckout}
          />

          <AuthModal
            isOpen={isAuthDialogOpen}
            onClose={() => setAuthDialogOpen(false)}
          />

          <ProfileModal
            isOpen={isProfileModalOpen}
            onClose={() => setIsProfileModalOpen(false)}
          />

          <CheckoutModal
            isOpen={isCheckoutModalOpen}
            onClose={() => setIsCheckoutModalOpen(false)}
          />
        </div>
      </CartProvider>
    </AuthProvider>
  );
}

export default App;