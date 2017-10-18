---
layout: data
title: Films
---
<table class="tablesorter">
    <thead>
        <th>IMDB</th>
        <th>Title</th>
        <th>Rating</th>
    </thead>
    <tbody>
    {% for item in site.data.films %}
        <tr>
            <td><a href="http://www.imdb.com/title/{{ item.Imdb }}/">{{ item.Imdb }}</a></td>
            <td>{{ item.Title}}</td>
            <td>{{ item.Rating}}</td> 
        </tr>
    {% endfor %}
    </tbody>
</table>
