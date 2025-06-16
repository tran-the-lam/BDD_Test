import { Product } from '../types';

export const products: Product[] = [
  {
    id: '1',
    name: 'Premium Wireless Headphones',
    description: 'High-quality wireless headphones with noise cancellation and 30-hour battery life.',
    price: 299.99,
    originalPrice: 399.99,
    image: 'https://images.pexels.com/photos/3394650/pexels-photo-3394650.jpeg?auto=compress&cs=tinysrgb&w=800',
    category: 'Electronics',
    inStock: true,
    rating: 4.8,
    reviews: 256,
    features: ['Noise Cancellation', '30hr Battery', 'Wireless', 'Premium Sound']
  },
  {
    id: '2',
    name: 'Smart Fitness Watch',
    description: 'Advanced fitness tracking with heart rate monitoring, GPS, and water resistance.',
    price: 249.99,
    image: 'https://images.pexels.com/photos/393047/pexels-photo-393047.jpeg?auto=compress&cs=tinysrgb&w=800',
    category: 'Electronics',
    inStock: true,
    rating: 4.6,
    reviews: 189,
    features: ['Heart Rate Monitor', 'GPS Tracking', 'Water Resistant', '7-Day Battery']
  },
  {
    id: '3',
    name: 'Ergonomic Office Chair',
    description: 'Comfortable ergonomic chair with lumbar support and adjustable height.',
    price: 399.99,
    originalPrice: 499.99,
    image: 'https://images.pexels.com/photos/586083/pexels-photo-586083.jpeg?auto=compress&cs=tinysrgb&w=800',
    category: 'Furniture',
    inStock: true,
    rating: 4.7,
    reviews: 143,
    features: ['Lumbar Support', 'Adjustable Height', 'Breathable Mesh', 'Ergonomic Design']
  },
  {
    id: '4',
    name: 'Professional Camera',
    description: 'High-resolution DSLR camera perfect for professional photography.',
    price: 899.99,
    image: 'https://images.pexels.com/photos/90946/pexels-photo-90946.jpeg?auto=compress&cs=tinysrgb&w=800',
    category: 'Electronics',
    inStock: true,
    rating: 4.9,
    reviews: 87,
    features: ['24MP Sensor', '4K Video', 'Weather Sealed', 'Dual Card Slots']
  },
  {
    id: '5',
    name: 'Luxury Sofa Set',
    description: 'Comfortable 3-piece sofa set with premium fabric and modern design.',
    price: 1299.99,
    originalPrice: 1599.99,
    image: 'https://images.pexels.com/photos/1350789/pexels-photo-1350789.jpeg?auto=compress&cs=tinysrgb&w=800',
    category: 'Furniture',
    inStock: true,
    rating: 4.5,
    reviews: 76,
    features: ['Premium Fabric', '3-Piece Set', 'Modern Design', 'Comfortable Cushions']
  },
  {
    id: '6',
    name: 'Wireless Gaming Mouse',
    description: 'High-precision gaming mouse with RGB lighting and programmable buttons.',
    price: 79.99,
    image: 'https://images.pexels.com/photos/2115256/pexels-photo-2115256.jpeg?auto=compress&cs=tinysrgb&w=800',
    category: 'Electronics',
    inStock: false,
    rating: 4.4,
    reviews: 234,
    features: ['RGB Lighting', 'Programmable Buttons', 'High DPI', 'Wireless']
  },
  {
    id: '7',
    name: 'Organic Cotton T-Shirt',
    description: 'Soft, comfortable t-shirt made from 100% organic cotton.',
    price: 29.99,
    image: 'https://images.pexels.com/photos/769733/pexels-photo-769733.jpeg?auto=compress&cs=tinysrgb&w=800',
    category: 'Clothing',
    inStock: true,
    rating: 4.3,
    reviews: 156,
    features: ['100% Organic Cotton', 'Soft Fabric', 'Machine Washable', 'Various Colors']
  },
  {
    id: '8',
    name: 'Coffee Maker Pro',
    description: 'Professional-grade coffee maker with multiple brewing options.',
    price: 199.99,
    originalPrice: 249.99,
    image: 'https://images.pexels.com/photos/324028/pexels-photo-324028.jpeg?auto=compress&cs=tinysrgb&w=800',
    category: 'Kitchen',
    inStock: true,
    rating: 4.6,
    reviews: 198,
    features: ['Multiple Brewing Options', 'Programmable Timer', 'Auto Shut-off', 'Large Capacity']
  }
];

export const categories = ['All', 'Electronics', 'Furniture', 'Clothing', 'Kitchen'];