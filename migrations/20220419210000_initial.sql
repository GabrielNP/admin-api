CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS users (
	user_id uuid NOT NULL DEFAULT uuid_generate_v4(),
	"name" varchar(50) NOT NULL,
	email varchar(200) NOT NULL,
	"password" text NOT NULL,
	created_at timestamptz NOT NULL DEFAULT NOW(),
	updated_at timestamptz NOT NULL DEFAULT NOW(),
	deleted_at timestamptz NULL,
	CONSTRAINT users_pk PRIMARY KEY (user_id),
	CONSTRAINT users_un UNIQUE (email)
);

CREATE TABLE IF NOT EXISTS roles (
	role_id uuid NOT NULL DEFAULT uuid_generate_v4(),
	"name" varchar(50) NOT NULL,
	description varchar(100) NULL,
	created_at timestamptz NOT NULL DEFAULT NOW(),
	updated_at timestamptz NOT NULL DEFAULT NOW(),
	deleted_at timestamptz NULL,
	CONSTRAINT roles_pk PRIMARY KEY (role_id)
);

CREATE TABLE IF NOT EXISTS resources (
	resource_id uuid NOT NULL DEFAULT uuid_generate_v4(),
	"name" varchar(100) NOT NULL,
	created_at timestamptz NOT NULL DEFAULT NOW(),
	updated_at timestamptz NOT NULL DEFAULT NOW(),
	deleted_at timestamptz NULL,
	CONSTRAINT resources_pk PRIMARY KEY (resource_id)
);

CREATE TABLE IF NOT EXISTS user_roles (
	user_id uuid NOT NULL,
	role_id uuid NOT NULL,
	created_at timestamptz NOT NULL DEFAULT NOW(),
	updated_at timestamptz NOT NULL DEFAULT NOW(),
	deleted_at timestamptz NULL,
	CONSTRAINT user_roles_pk PRIMARY KEY (user_id,role_id),
    CONSTRAINT user_roles_fk_1 FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    CONSTRAINT user_roles_fk_2 FOREIGN KEY (role_id) REFERENCES roles(role_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS role_resources (
	role_id uuid NOT NULL,
	resource_id uuid NOT NULL,
	created_at timestamptz NOT NULL DEFAULT NOW(),
	updated_at timestamptz NOT NULL DEFAULT NOW(),
	deleted_at timestamptz NULL,
	CONSTRAINT role_resources_pk PRIMARY KEY (resource_id,role_id),
	CONSTRAINT role_resources_fk_1 FOREIGN KEY (role_id) REFERENCES roles(role_id) ON DELETE CASCADE,
	CONSTRAINT role_resources_fk_2 FOREIGN KEY (resource_id) REFERENCES resources(resource_id) ON DELETE CASCADE
);


=====DOWN

DROP TABLE IF EXISTS user_roles;
DROP TABLE IF EXISTS role_resources;
DROP TABLE IF EXISTS roles;
DROP TABLE IF EXISTS resources;
DROP TABLE IF EXISTS users;
