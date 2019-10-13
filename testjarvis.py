{% extends "layout.html" %} {% block body %}
<style>
  #contact {
    color: chartreuse;
    font-size: large;
  }
</style>
<!-- Page Header -->
<header
  class="masthead"
  style="background-image: url('{{url_for('static',filename='img/home-bg.jpg')}}')"
>
  <div class="overlay"></div>
  <div class="container">
    <div class="row">
      <div class="col-lg-8 col-md-10 mx-auto">
        <div class="site-heading">
          <h1>DevViju</h1>
          <span class="subheading">Coder, Ultimate Legend</span>
          <pre> <span id="contact">Contact: 9079999751
           8094298181
         </span></pre>
        </div>
      </div>
    </div>
  </div>
</header>

<!-- Main Content -->
<div class="container">
  <div class="row">
    <div class="col-lg-8 col-md-10 mx-auto">
      <div class="post-preview">
        <a href="post.html">
          <h2 class="post-title">
            Man must explore, and this is exploration at its greatest
          </h2>
          <h3 class="post-subtitle">
            Problems look mighty small from 150 miles up
          </h3>
        </a>
        <p class="post-meta">
          Posted by
          <a href="#">Start Bootstrap</a>
          on September 24, 2019
        </p>
      </div>
      <hr />
      <div class="post-preview">
        <a href="post.html">
          <h2 class="post-title">
            I believe every human has a finite number of heartbeats. I don't
            intend to waste any of mine.
          </h2>
        </a>
        <p class="post-meta">
          Posted by
          <a href="#">Start Bootstrap</a>
          on September 18, 2019
        </p>
      </div>
      <hr />
      <div class="post-preview">
        <a href="post.html">
          <h2 class="post-title">
            Science has not yet mastered prophecy
          </h2>
          <h3 class="post-subtitle">
            We predict too much for the next year and yet far too little for the
            next ten.
          </h3>
        </a>
        <p class="post-meta">
          Posted by
          <a href="#">Start Bootstrap</a>
          on August 24, 2019
        </p>
      </div>
      <hr />
      <div class="post-preview">
        <a href="post.html">
          <h2 class="post-title">
            Failure is not an option
          </h2>
          <h3 class="post-subtitle">
            Many say exploration is part of our destiny, but it’s actually our
            duty to future generations.
          </h3>
        </a>
        <p class="post-meta">
          Posted by
          <a href="#">Start Bootstrap</a>
          on July 8, 2019
        </p>
      </div>
      <hr />
      <!-- Pager -->
      <div class="clearfix">
        <a class="btn btn-primary float-right" href="#">Older Posts &rarr;</a>
      </div>
    </div>
  </div>
</div>

{% endblock %}
