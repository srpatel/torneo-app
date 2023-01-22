<script>
  import Router, { location, link } from "svelte-spa-router";
  import Home from "./Home.svelte";
  import About from "./About.svelte";
  import Number from "./Number.svelte";

  let number = 0;

  function randomiseNumber() {
    number = Math.floor(Math.random() * 100);
  }

  randomiseNumber();
</script>

<div class="navbar bg-base-100">
  <div class="navbar-start">
    <a href="/" class="btn btn-ghost normal-case text-xl">Torneo</a>
  </div>
  <div class="navbar-center">
    <ul class="menu menu-horizontal px-1">
      <li><a href="/#/about">About</a></li>
      <li>
        <a href="/#/number/{number}" on:click={randomiseNumber}>Number</a>
      </li>
    </ul>
  </div>
  <div class="navbar-end" />
</div>

<Router
  routes={{
    "/": Home,
    "/about": About,
    "/number/:number": Number,
  }}
/>
