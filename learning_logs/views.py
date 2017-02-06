from django.shortcuts import render, get_object_or_404
from .models import Topic, Entry

from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from .forms import TopicForm, EntryForm

from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Show all topics."""
    topics = (Topic.objects.
        filter(owner=request.user).order_by('date_added'))
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = get_object_or_404(Topic, topic_id)
    # Make sure the topic belong to the current user.
    check_topic_owner(request, topic)

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic' : topic, 'entries' : entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # Request may be GET, we can safely return to users a blank form
        form = TopicForm()   
    else:
        # Process and POST data submitted, Redirect back to Topics page
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form' : form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry"""
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belong to the current user.
    check_topic_owner(request, topic)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                            args=[topic_id]))


    context = {'topic' : topic ,'form' : form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit an entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # Make sure the topic belong to the current user.
    check_topic_owner(request, topic)

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                            args=[topic.id]))

    context = {'entry' : entry, 'topic' : topic, 'form' : form}
    return render(request, 'learning_logs/edit_entry.html', context)

def check_topic_owner(request, topic):
    """If request user is not the owner, raise 404"""
    if topic.owner != request.user:
        raise Http404












