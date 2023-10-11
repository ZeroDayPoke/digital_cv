// config/database.js

import Sequelize from "sequelize";
import "../utils/loadEnv.js";

const env = process.env.NODE_ENV || "development";

/**
 * Configuration object for database connection.
 * @typedef {Object} DbConfig
 * @property {string} username - The username for the database connection.
 * @property {string} password - The password for the database connection.
 * @property {string} database - The name of the database to connect to.
 * @property {string} host - The host for the database connection.
 * @property {string} dialect - The dialect for the database connection. Defaults to "mysql".
 * @property {boolean|function} logging - Whether to log database queries. If set to true, logs to console. If set to false, disables logging. If set to a function, calls that function with the query and execution time.
 */
const dbConfig = {
  username: process.env.DB_USER,
  password: process.env.DB_PASS,
  database: process.env.DB_NAME,
  host: process.env.DB_HOST,
  dialect: process.env.DB_DIALECT || "mysql",
  logging: env === "development" ? console.log : false,
};

/**
 * Creates a new Sequelize instance with the provided configuration options.
 * @param {string} dbConfig.database - The name of the database to connect to.
 * @param {string} dbConfig.username - The username to use when connecting to the database.
 * @param {string} dbConfig.password - The password to use when connecting to the database.
 * @param {string} dbConfig.host - The host to connect to.
 * @param {string} dbConfig.dialect - The dialect of the database to connect to.
 * @param {boolean} dbConfig.logging - Whether or not to log SQL queries.
 * @returns {Sequelize} A new Sequelize instance.
 */
const db = new Sequelize(
  dbConfig.database,
  dbConfig.username,
  dbConfig.password,
  {
    host: dbConfig.host,
    dialect: dbConfig.dialect,
    logging: dbConfig.logging,
  }
);

export default db;
