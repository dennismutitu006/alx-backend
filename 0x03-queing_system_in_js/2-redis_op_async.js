import { createClient } from 'redis';
import redis from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}
//promisify is used to convert call back based func into promise based func.

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  try {
      const value = await getAsync(schoolName);
      console.log(value);
  } catch (err) {
      console.log(`Error: ${err}`);
  }
}
// Call the functions at EOF
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
