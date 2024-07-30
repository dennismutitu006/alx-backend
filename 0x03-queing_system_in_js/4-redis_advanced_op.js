import redis from 'redis';
const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});
client.on('error', (err) => {
  console.log(`Error: ${err.message}`);
});

function setNewHash() {
  client.hset('HolbertonSchools', 'Portland', 50, redis.print);
  client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
  client.hset('HolbertonSchools', 'New York', 20, redis.print);
  client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
  client.hset('HolbertonSchools', 'Cali', 40, redis.print);
  client.hset('HolbertonSchools', 'Paris', 2, redis.print);
}

function displayHash() {
  client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
      console.log(`Error: ${err}`);
    } else {
      console.log(reply);
    }
  });
}
//store the hash values
setNewHash();
// display the stored hash values
displayHash();
