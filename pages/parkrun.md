---
layout: data
title: ParkRun
---

<table class="tablesorter">
    <thead>
          <th>Number</th>
          <th>Time</th>
          <th>Age Grade</th>
  </thead>
  <tbody>
    {% for event in site.data.parkrun %}
  <tr>
    <td>{{ event.Run }}</td>
    <td>{{ event.Time}}</td>
    <td>{{ event.AgeGrade}}</td> 
  </tr>
      {% endfor %}
   </tbody>
</table>
