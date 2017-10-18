---
layout: data
title: Mac Apps
---

If I ever returned from a iOS only to a Mac setup these are the apps to be installed first.

<table class="tablesorter">
    <thead>
      <th>Apps</th>
    </thead>
    <tbody>
      {% for item in site.data.mac-apps %}
      <tr>
        <td>{{ item.App }}</td>
      </tr>
      {% endfor %}
   </tbody>
</table>
