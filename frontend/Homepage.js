import React from 'react';
import ProductList from './ProductList';
import ProductRecommendations from './ProductRecommendations';

const Homepage = () => {
  return (
    <div className="homepage">
      <h1>Welcome to the Print-on-Demand Platform</h1>
      <ProductRecommendations />
      <ProductList />
    </div>
  );
};

export default Homepage;

