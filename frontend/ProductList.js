import React from 'react';
import ProductCard from './ProductCard';

const ProductList = () => {
  const products = [
    {
      id: 1,
      name: 'Custom T-Shirt',
      description: 'Design your own unique T-Shirt',
      price: 29.99,
      image: 'https://via.placeholder.com/150x150',
    },
    {
      id: 2,
      name: 'Personalized Mug',
      description: 'Create a personalized mug with your favorite photo or design',
      price: 19.99,
      image: 'https://via.placeholder.com/150x150',
    },
    {
      id: 3,
      name: 'Custom Phone Case',
      description: 'Protect your phone with a stylish custom case',
      price: 14.99,
      image: 'https://via.placeholder.com/150x150',
    },
  ];

  return (
    <div className="product-list">
      <h2>Featured Products</h2>
      {products.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
};

export default ProductList;

