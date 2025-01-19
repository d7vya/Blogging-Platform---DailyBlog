from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from Home.models import *
from guardian.shortcuts import assign_perm
from django.db.models import Q
# Create your views here.
   
def blog(request):
    edit=request.GET.get('edit')
    print(edit)
   
    blogid=request.GET.get('blogid')
    print(blogid)
    blog=Blog.objects.get(id=blogid)
    print(blog)
  
    if edit=='change' and request.user.has_perm('Home.change_blog',blog):
        return redirect(f'/addBlog?edit={blogid}')
    elif edit=='delete' and request.user.has_perm('Home.delete_blog',blog):
        message='Blog'+' '+ blog.title+' '+'successfully deleted'
        blog.delete()
        
    else:
        message='you are not allowed to make changes to your blog'    
    return redirect(f'/dashbord?message={message}')




def home(request):
    popular=Blog.objects.all().order_by('-view_count')[:4]
    latest=Blog.objects.all().order_by('-datentime')[:4]
    context={'popular':popular,'latest':latest}
    return render(request,'homepage.html',context)

def login_(request):
    next_url=request.GET.get('next','/')
    context={'next':next_url}
    if request.method=='POST':
        username,password=request.POST['username'],request.POST['password']
        if User.objects.filter(username=username).exists():
            user= authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect(next_url)
            else:
                context['message']='Incorrect Password'
                return render(request,'login.html',context)
        else:
            
                context['message']='Username does not exist'
                return render(request,'login.html',context)
           
    return render(request,'login.html',context)
   
    

def logout_(request):
    logout(request)
    return redirect('/')

@login_required(redirect_field_name='next')
def dashboard(request):
    
    message=request.GET.get('message',None)
    userinfo=request.GET.get('open','/')
    if userinfo=='comment':
        comments=Comment.objects.filter(username=request.user)
        print(comment)
        return render(request,'dashboard.html',{'comments':comments})

    else:
        blogs=Blog.objects.filter(username=request.user)
        print(blogs)   
        return render(request,'dashboard.html',{'blogs':blogs,'message':message})

@login_required(redirect_field_name='next')
def addBlog(request):
    username=request.user
    query=request.GET.get('edit','')
    print(query)
    context={}
    if query:
            blog=Blog.objects.get(id=query)
            context['blog']=blog
    
    if username.has_perm('Home.add_blog') or(query):
        
        if request.method=='POST':
           
            title=request.POST['title']
            desc=request.POST['desc']
            body=request.POST['body']
            tags=request.POST.getlist('tag')
            cate=request.POST['category'] 
            print(request.POST['button'])
            if request.POST['button']!='submit':
                
                blog=Blog.objects.get(id=request.POST['button'])
                message=f'change on {title} executed'   
            else:  
                  
                blog= Blog(username=username)
                
                message=f'{title} created successfully '
                
            blog.body=body
            
            blog.title=title
            blog.desc=desc
            
            cate=Category.objects.get(name=cate)
            
            blog.category=cate
            blog.save()
            tags_v = []
            for tag_name in tags:
                if Tag.objects.filter(name=tag_name).exists():
                    tags_v.append(tag_name)    
            blog.tags.set(tags_v)
            blog.save()
            
            if not query:
                assign_perm('change_blog',request.user,blog)
                assign_perm('delete_blog',request.user,blog)
            
            return redirect(f'/dashboard?message={message}')
        
        
         
        tags= Tag.objects.all()
        category=Category.objects.all()
        context['tags']=tags
        context['category']=category
         
        return render(request,'addnew.html',context)        
    else:
        alert="you don't have permission to do this"
        return render(request,'addnew.html',{'alert': alert})
    


def blogs(request):
    categorys=Category.objects.all()
    tags=Tag.objects.all()
    blogs=Blog.objects.all()
    filters=request.GET.get('filter','')
    search=request.GET.get('search','')
    cat_s='all'
    sort_s='-view_count'
    tag_s='any'
    if request.method=='POST' and filters:
        tag_s=request.POST.getlist('tags', [])
        cat_s=request.POST.get('category',cat_s)
        sort_s=request.POST.get('sort',sort_s)
        if search:
            print(search)
            blogs=blogs.filter(Q(title__icontains=search) | Q(desc__icontains=search))
        if cat_s !='all':
            cat=Category.objects.get(name=cat_s)
            blogs=blogs.filter(category=cat)
            if tag_s and tag_s!=['any']:
                
                blogs=blogs.filter(tags__in=tag_s)
                
        else:
            if tag_s and tag_s!=['any']:
                blogs=blogs.filter(tags__in=tag_s)
                
        
           
    
    
    elif request.method=='POST' and not filters :
        search=request.POST['search']
        print(search.title())
        blogs=blogs.filter(Q(title__icontains=search) | Q(desc__icontains=search))
        
        
    blogs=blogs.order_by(sort_s).distinct()     
        
    print(tag_s)   
    context={'blogs':blogs,'tags':tags,'categorys':categorys,'cat_s':cat_s,'sort_s':sort_s,'tag_s':tag_s,'search':search}
    return render(request,'blogs.html',context)

def register(request):
    next_url= request.GET.get('next','/')
    context={'next':next_url}
    if request.method=='POST':
        username,email,lname,fname,password=request.POST['username'],request.POST['email'],request.POST['lname'],request.POST['fname'],request.POST['password']
       
        if User.objects.filter(username=username).exists():
            context['message']='This username not available'
            context['post']=request.POST
            return render(request,'register.html',context)
        elif User.objects.filter(email=email).exists():
            context['message']='This email already exist'
            context['post']=request.POST
            return render(request,'register.html',context)
        
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            
            user.last_name=lname
            user.first_name=fname
            user.save()
            group=Group.objects.get(name='user_group')
            user.groups.set([group])
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect(next_url)
        
    return render(request,'register.html',context)


@login_required(redirect_field_name='next')
def blogpost(request,blogid):
    blog= Blog.objects.get(id=blogid)
    comments=Comment.objects.filter(blog=blogid)
    context={'blog':blog,'comments':comments}
    if request.user != blog.username:
        blog.view_count+=1
        blog.save()
    return render(request,'blogpost.html',context)



def comment(request,blogid):
    blog=Blog.objects.get(id=blogid)
    context={}
    if request.POST['submit']=='post':
        if request.user.has_perm('Home.add_comment'):   
            
            comment=Comment(blog=blog)
        
            comment.username=request.user
            comment.content=request.POST['comment']
            comment.save()
            
            blog.save()
            assign_perm('delete_comment' ,request.user,comment)
            assign_perm('delete_comment' ,blog.username,comment)
        else:
            context['message']="You don't have permission to post a comment on any blog"
    elif request.POST['submit']=='delete':
        cmid=request.GET.get('comment')
        comment=Comment.objects.get(id=cmid)        
        comment.delete()
              
    comments=Comment.objects.filter(blog=blogid)
    context['blog']=blog
    context['comments']=comments
    blog.commen_count=len(comments)
    blog.save()
    return render(request,'blogpost.html',context)



    

def restrictuser(request,username):
    
  
    user=User.objects.get(username=username)
    print('actions' in request.POST.keys())
    if 'actions' in request.POST.keys():
        action=request.POST['actions']
        print(action)
        if action=='ban':
            
            group=Group.objects.get(name='ban_user')
        elif request.POST['actions']=='unban':
            group=Group.objects.get(name='user_group')    
        print('yes')  
         
        user.groups.set([group])
    if request.GET.get('page',''):
        return redirect('/userpage')
    else:    
        return redirect('/blogs')

def userpage(request):
    users=User.objects.all()
    return render(request,'users.html',{'users':users})    