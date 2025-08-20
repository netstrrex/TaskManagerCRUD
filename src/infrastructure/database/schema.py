SCHEMA = """
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'task_status') THEN
        CREATE TYPE task_status AS ENUM ('created', 'in_progress', 'done');
    END IF;
END
$$;
CREATE TABLE IF NOT EXISTS tasks(
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    title VARCHAR(128) NOT NULL,
    description TEXT NOT NULL,
    status task_status NOT NULL DEFAULT 'created'
);"""
