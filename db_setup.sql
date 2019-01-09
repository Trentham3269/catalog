CREATE TABLE categories (  
  id SERIAL PRIMARY KEY,  
  name VARCHAR(50) NOT NULL
);

CREATE TABLE items (
  id SERIAL PRIMARY KEY, 
  title VARCHAR(50) NOT NULL,
  description VARCHAR(250) NOT NULL,
  cat_id INTEGER REFERENCES categories(id)
);

INSERT INTO categories (id, name) VALUES (1, 'Soccer');
INSERT INTO categories (id, name) VALUES (2, 'Basketball');
INSERT INTO categories (id, name) VALUES (3, 'Baseball');
INSERT INTO categories (id, name) VALUES (4, 'Frisbee');
INSERT INTO categories (id, name) VALUES (5, 'Snowboarding');
INSERT INTO categories (id, name) VALUES (6, 'Rock Climbing');
INSERT INTO categories (id, name) VALUES (7, 'Football');
INSERT INTO categories (id, name) VALUES (8, 'Surfing');
INSERT INTO categories (id, name) VALUES (9, 'Hockey');

INSERT INTO items (id, title, description, cat_id) VALUES (1, 'Boots', 'The latest in comfort, style and cost!', 1);
INSERT INTO items (id, title, description, cat_id) VALUES (2, 'Indoor ball', 'As used in the NBA', 2);
INSERT INTO items (id, title, description, cat_id) VALUES (3, 'Outdoor ball', 'Great for local pickup games', 2);
INSERT INTO items (id, title, description, cat_id) VALUES (4, 'Net', 'The only net for that full swoosh sound', 2);
INSERT INTO items (id, title, description, cat_id) VALUES (5, 'Bat', 'What a beautiful piece of hickory', 3);
INSERT INTO items (id, title, description, cat_id) VALUES (6, 'Ball', 'Handmade - childrens fingers make for exquisite stitching', 3);
INSERT INTO items (id, title, description, cat_id) VALUES (7, 'Frisbee', 'Well...duh!', 4);
INSERT INTO items (id, title, description, cat_id) VALUES (8, 'Snowboard', 'Boutique board made from carbon fibre, the optimum mix of light-weight strength and profit margin', 5);
INSERT INTO items (id, title, description, cat_id) VALUES (9, 'Goggles', 'Wrap around UV protection so you can see when you are being ripped off', 5);
INSERT INTO items (id, title, description, cat_id) VALUES (10, 'Gloves', 'Microfibre lining for warmth and stuff', 5);
INSERT INTO items (id, title, description, cat_id) VALUES (11, 'Rope', 'Supports a climber up to 200kgs (as long as their fingers do)', 6);
INSERT INTO items (id, title, description, cat_id) VALUES (12, 'Rocks', 'Do we really sell these???', 6);
INSERT INTO items (id, title, description, cat_id) VALUES (13, 'Football', 'The good old pigskin', 7);
INSERT INTO items (id, title, description, cat_id) VALUES (14, 'Helmet', 'Best worn before your time in the concussion protocol', 7);
INSERT INTO items (id, title, description, cat_id) VALUES (15, 'Shoulder pads', 'Bigger than those in an 80s sitcom', 7);
INSERT INTO items (id, title, description, cat_id) VALUES (16, 'Surfboard', 'Almost obligatory', 8);
INSERT INTO items (id, title, description, cat_id) VALUES (17, 'Stick', 'Field or ice?', 9);
INSERT INTO items (id, title, description, cat_id) VALUES (18, 'Ice Skates', 'Well that explains the stick type', 9);