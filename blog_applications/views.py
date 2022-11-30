from blog_applications.models import users,blogs
#
# most_liked=max(blogs,key=lambda b:len(b.get("liked_by")))
# print(most_liked)
#
# less_following=min(users,key=lambda u:len(u.get("following")))
# print(less_following)
#
# post_of_specific=[ blog for blog in blogs if blog.get("userId")==2]
# print(post_of_specific)

# users.sort(key=lambda u:len(u.get("following")),reverse=True)
# print(users)

# userId=1
# followes_of_specific=[u.get("username") for u in users if userId in u.get("following")]
# print(followes_of_specific)
#
# logged_user=3
# all_user_id=[u.get("id") for u in users]
# all_user_id.remove(logged_user)
# print(all_user_id)
# logged_user_following=[u.get("following") for u in users if u.get("id")==logged_user].pop()
# print(logged_user_following)
# print(set(all_user_id)-set(logged_user_following))

# uname="akhil"
# passwrd=123
# user=[u for u in users if u.get("username")==uname and u.get("password")==passwrd]
# if len(user)>0:
#     print("login sucess")
# else:
#     print("login denied")

blog_count={}
for blog in blogs:
    user_id=blog.get("userId")
    user_name = [user.get("username") for user in users if user.get("id") == user_id].pop()
    if user_name in blog_count:
        blog_count[user_name]+=1
    else:
        blog_count[user_name]=1
print(blog_count)
a_user=max(blog_count,key=lambda k:blog_count[k])
print(a_user)