So, as I have been given a task to do teh analysis and some prediction of a Email Marketing Campaign. I have done the task within the deadline and made sure that my analysis and insights of this task show my skills and understading of the Data and also the Machine Learning Models.

So first I have clubbed the data of three .csv files into a single file and then I have made sure that there are no duplicates in the email_id column (if there some I would have checked the other column and then decided whether to keep them or delete them).

I have calculated the precentage of users who openede the email and who clicked the email.

Now I have used RandomForestClassifier to have a look at the prediction and evaluated the model using confusion matrix and ROC_AUC_score. Before that I have calculated the probability of each email_id to be clicked.

Now I have come to know that the model is unable to classify the clicked email id properly as they are in very low percentage 2.12% (Model is Playing safe). The ROC_AUC_score of the model is 0.4819 which is worse than random(ranfom = 0.5)

So now I have plotted the feature importance barplot, I have observed that Time and past purchase experience of the user have a lot of toll on the click-rate (no.of clicked_email_ids / total no. of email_ids).

So I have individually clssified both the features into subsets and observed the variation. The users who have done 20+ purchases have higher click-rate compared to fewer purchased users, emails sent at 10pm night have the higher click-rate compared to that of the other hours.

Now as I have already have the predicted probabilities of the each email_id from the model, I have taken top_percent( we can take top 10%, 20%, 30% according to our convenience, but if you increase the percent the sample space gonna increase but improvement decreases) and done automated A/B testing to find of the  Estimated Improvement.

So I have found out that we gonna get almost 300% improvement if we send emails carefully to the users whose clicking probability is in top 10%.

So I hope my anwers have given the good insights, which can be useful and can be strategized well and implemented to yield good click-rate which is going to help the company. 