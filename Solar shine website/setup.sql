INSERT INTO users (name, surname, phone, email, address) VALUES
('Alice', 'Johnson', '123-456-7890', 'alice.johnson@example.com', '123 Solar St, Sunnytown'),
('Bob', 'Smith', '987-654-3210', 'bob.smith@example.com', '456 Energy Ave, Sol City'),
('Charlie', 'Brown', '555-123-4567', 'charlie.brown@example.com', '789 Eco Way, Greentown'),
('Diana', 'Lopez', '222-333-4444', 'diana.lopez@example.com', '321 Bright Blvd, Cleartown'),
('Ethan', 'Williams', '111-222-3333', 'ethan.williams@example.com', '654 Shine Rd, Solana');

INSERT INTO orders (userID, created_at, scheduled_at, status, notes) VALUES
(1, '2025-09-01 10:00:00', '2025-09-10 09:00:00', 'Pending', 'Customer prefers early morning'),
(2, '2025-09-02 11:30:00', '2025-09-11 14:00:00', 'Completed', 'Routine cleaning'),
(3, '2025-09-03 09:15:00', '2025-09-12 13:00:00', 'Pending', 'Inspect loose panel'),
(4, '2025-09-04 08:45:00', '2025-09-13 10:30:00', 'Completed', 'Heavy bird droppings noted last time'),
(5, '2025-09-05 12:00:00', '2025-09-14 11:00:00', 'Pending', 'Customer wants technician to call before arrival');