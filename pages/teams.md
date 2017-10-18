---
layout: data
title: Teams seen live
---

<table class="tablesorter">
    <thead>
      <th>Teams</th>
    </thead>
    <tbody>
      {% for item in site.data.teams %}
      <tr>
        <td>{{ item.Teams }}</td>
      </tr>
      {% endfor %}
   </tbody>
</table>
