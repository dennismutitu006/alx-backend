import kue from 'kue';
//array of blacklisted numbers
const blackList = ['4153518780', '4153518781'];
//Function to send notifications
const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);

  if(blackList.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, 
               with message: ${message}`);
  done();
}

const queue = kue.createQueue();
//process jobs in the queue
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
