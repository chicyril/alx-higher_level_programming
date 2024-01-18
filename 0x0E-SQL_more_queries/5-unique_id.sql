-- creates the table unique_id without error

CREATE TABLE IF NOT EXISTS `unique_id` (
    `id` UNIQUE INT DEFAULT 1,
    `name` VARCHAR(256)
);
