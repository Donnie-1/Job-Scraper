const Pool = require('pg').Pool;

const pool = new Pool({
    user: 'samevstigneev',
    password: 'password',
    host: 'localhost',
    port: 5432,
    database: 'tododb'
});

module.exports = pool;