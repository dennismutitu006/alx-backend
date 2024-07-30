import kue from 'kue';
import redis from 'redis';

//create a redisclient
const redisClient = redis.createClient();

//create a kue queue
const queue = kue.createQueue({
  redis: {
    host: 'localhost',
    port: 6379
  }
});

//create a job data object
const jobData = {
  phoneNumber: '0792420040',
  message: 'Hello there'
};

//create a job and add it to the queue
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) {
      console.log(`Notification job failed: ${err.message}`);
    } else {
      console.log(`Notification job created: ${job.id}`);
    }
  });

//handle job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

//handle failure
job.on('failed', (errorMessage) => {
  console.log(`Notification job failed: ${errorMessage}`);
});
