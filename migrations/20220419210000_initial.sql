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
	is_active bool NOT NULL DEFAULT false,
	is_admin bool NOT NULL DEFAULT false,
	CONSTRAINT users_pk PRIMARY KEY (user_id),
	CONSTRAINT users_un UNIQUE (email)
);

INSERT INTO users
	("name", email, "password", is_active, is_admin)
VALUES('Admin', 'admin@admin.com', crypt('admin', gen_salt('bf', 8)), true, true);

CREATE TABLE IF NOT EXISTS roles (
	role_id uuid NOT NULL DEFAULT uuid_generate_v4(),
	"name" varchar(50) NOT NULL,
	description varchar(100) NULL,
	created_at timestamptz NOT NULL DEFAULT NOW(),
	updated_at timestamptz NOT NULL DEFAULT NOW(),
	deleted_at timestamptz NULL,
	CONSTRAINT roles_pk PRIMARY KEY (role_id)
);

CREATE TABLE IF NOT EXISTS projects (
	project_id uuid NOT NULL DEFAULT uuid_generate_v4(),
	"name" varchar(50) NOT NULL,
	created_at timestamptz NOT NULL DEFAULT NOW(),
	updated_at timestamptz NOT NULL DEFAULT NOW(),
	deleted_at timestamptz NULL,
	CONSTRAINT projects_pk PRIMARY KEY (project_id)
);

CREATE TABLE IF NOT EXISTS user_roles (
	user_role_id uuid NOT NULL DEFAULT uuid_generate_v4(),
	role_id uuid NOT NULL,
	user_id uuid NOT NULL,
	project_id uuid NOT NULL,
	created_at timestamptz NOT NULL DEFAULT NOW(),
	updated_at timestamptz NOT NULL DEFAULT NOW(),
	deleted_at timestamptz NULL,
	CONSTRAINT user_roles_pk PRIMARY KEY (user_role_id),
    CONSTRAINT user_roles_fk_1 FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE RESTRICT,
    CONSTRAINT user_roles_fk_2 FOREIGN KEY (role_id) REFERENCES roles(role_id) ON DELETE RESTRICT,
    CONSTRAINT user_roles_fk_3 FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE RESTRICT
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
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS roles;
DROP TABLE IF EXISTS users;
