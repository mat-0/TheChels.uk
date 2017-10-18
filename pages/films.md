---
layout: data
title: Films
---
<table class="tablesorter">
    <thead>
        <th>Title</th>
        <th>Rating</th>
        <th>Imdb</th>
    </thead>
    <tbody>
    {% for item in site.data.films %}
        <tr>
            <td>{{ item.Title }}</td>
            <td>{{ item.Rating }}</td>
            <td><a href="http://www.imdb.com/title/{{ item.Imdb }}/">{{ item.Imdb }}</a></td>
        </tr>
    {% endfor %}
    </tbody>
</table>
