CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS users (
	user_id uuid NOT NULL DEFAULT uuid_generate_v4(),
	"name" varchar(200) NOT NULL,
	email varchar(200) NOT NULL,
	"password" text NOT NULL,
	created_at timestamptz NOT NULL DEFAULT NOW(),
	updated_at timestamptz NOT NULL DEFAULT NOW(),
	deleted_at timestamptz NULL,
	CONSTRAINT users_pk PRIMARY KEY (user_id),
	CONSTRAINT users_un UNIQUE (email)
);

INSERT INTO users
	("name", email, "password", created_at, updated_at)
VALUES('Admin', 'admin@amdin.com', crypt('admin', gen_salt('bf', 8)), now(), now());

CREATE TABLE IF NOT EXISTS roles (
	role_id uuid NOT NULL DEFAULT uuid_generate_v4(),
	"name" varchar(50) NOT NULL,
	description varchar(100) NULL,
	created_at timestamptz NOT NULL DEFAULT NOW(),
	updated_at timestamptz NOT NULL DEFAULT NOW(),
	deleted_at timestamptz NULL,
	CONSTRAINT roles_pk PRIMARY KEY (role_id)
);

CREATE TABLE IF NOT EXISTS user_roles (
	user_id uuid NOT NULL DEFAULT uuid_generate_v4(),
	role_id uuid NOT NULL,
	created_at timestamptz NOT NULL DEFAULT NOW(),
	updated_at timestamptz NOT NULL DEFAULT NOW(),
	deleted_at timestamptz NULL,
	CONSTRAINT user_roles_pk PRIMARY KEY (user_id,role_id),
    CONSTRAINT user_roles_fk_1 FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    CONSTRAINT user_roles_fk_2 FOREIGN KEY (role_id) REFERENCES roles(role_id) ON DELETE CASCADE
);

CREATE TABLE blacklist_tokens (
	id uuid NOT NULL DEFAULT uuid_generate_v4(),
	"token" varchar(300) NOT NULL,
	CONSTRAINT blacklist_tokens_pk PRIMARY KEY (id)
);
COMMENT ON TABLE public.blacklist_tokens IS 'Tokens that cannot be used anymore.';


=====DOWN

DROP TABLE IF EXISTS blacklist_tokens;
DROP TABLE IF EXISTS user_roles;
DROP TABLE IF EXISTS roles;
DROP TABLE IF EXISTS users;
