INSERT INTO users (username, email, password)
VALUES
  ('admin', 'admin@example.com', 'admin123'),
  ('user1', 'user1@example.com', 'user123');

INSERT INTO stores (owner_id, name, description)
VALUES
  (1, 'My Store', 'Welcome to my store!'),
  (2, 'User1\'s Store', 'This is User1\'s store.');

INSERT INTO designs (user_id, store_id, name, description, image)
VALUES
  (1, 1, 'Custom T-Shirt', 'Design your own unique T-Shirt', 'https://via.placeholder.com/150x150'),
  (1, 1, 'Personalized Mug', 'Create a personalized mug with your favorite photo or design', 'https://via.placeholder.com/150x150'),
  (2, 2, 'Custom Phone Case', 'Protect your phone with a stylish custom case', 'https://via.placeholder.com/150x150');

