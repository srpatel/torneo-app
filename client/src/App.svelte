<script>
  import { setContext } from "svelte";
  import { writable } from "svelte/store";

  import Router, { location, link } from "svelte-spa-router";
  import Home from "./Home.svelte";
  import About from "./About.svelte";
  import Tournament from "./Tournament.svelte";
  import CreateTournament from "./CreateTournament.svelte";

  import HomeSvg from "./svg/home.svg";
  import InfoSvg from "./svg/info.svg";
  import TournamentSvg from "./svg/tournament.svg";

  const contextAction = writable(null);
  setContext("torneo-context-action", contextAction);

  $: $location, ($contextAction = null);
</script>

<div class="navbar bg-base-100">
  <div class="navbar-start" />
  <div class="navbar-center">
    <a href="/" class="btn btn-ghost normal-case text-xl" use:link>Torneo</a>
  </div>
  <div class="navbar-end">
    {#if $contextAction}
      <a
        href={$contextAction.href}
        class="btn btn-ghost normal-case text-xl"
        use:link>{$contextAction.text}</a
      >
    {/if}
  </div>
</div>

<div
  class="absolute inset-y-16 p-4 w-full flex flex-col items-center overflow-auto"
>
  <div class="my-auto">
    <Router
      routes={{
        "/": Home,
        "/about": About,
        "/tournament": CreateTournament,
        "/tournament/:code": Tournament,
      }}
    />
  </div>
</div>

<div class="btm-nav">
  <a class:active={$location == "/"} href="/" use:link>
    <img alt="Home" src={HomeSvg} width="24" height="24" />
  </a>
  <!-- Link to last active tournament -->
  <a
    class:active={$location?.startsWith("/tournament")}
    href="/tournament"
    use:link
  >
    <img alt="Tournament" src={TournamentSvg} width="24" height="24" />
  </a>
  <a class:active={$location == "/about"} href="/about" use:link>
    <img alt="About" src={InfoSvg} width="24" height="24" />
  </a>
</div>
