<script>
  import Router, { location, link } from "svelte-spa-router";
  import Home from "./Home.svelte";
  import About from "./About.svelte";
  import Number from "./Number.svelte";

  let number = 0;

  function randomiseNumber() {
    number = Math.floor(Math.random() * 500);
  }

  randomiseNumber();
</script>

<h1>Torneo</h1>

<nav>
  <a href="/">Home</a>
  <a href="/#/about">About</a>
  <a href="/#/number/{number}" on:click={randomiseNumber}>Number</a>
</nav>

<Router
  routes={{
    "/": Home,
    "/about": About,
    "/number/:number": Number,
  }}
/>
