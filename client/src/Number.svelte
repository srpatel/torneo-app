<script>
  import { onMount } from "svelte";
  import { push } from "svelte-spa-router";

  export let params;

  let responseNumber = null;

  $: params, fetchNumberDetails();
  async function fetchNumberDetails() {
    const res = await fetch(
      import.meta.env.VITE_API_BASE_URL + `/number/` + params.number
    );
    responseNumber = await res.json();
  }

  async function handleRandomiseNumber() {
    const number = Math.floor(Math.random() * 100);
    push(`/number/${number}`);
  }

  async function handleCreateNumber() {
    const res = await fetch(import.meta.env.VITE_API_BASE_URL + `/number/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        number: params.number,
      }),
    });
    responseNumber = await res.json();
  }
</script>

<div class="flex-1 flex items-center justify-center flex-col">
  <div class="stats shadow">
    <div class="stat">
      <div class="stat-title">Number</div>
      <div class="stat-value text-primary">{params.number}</div>
      <div class="stat-desc">What a cool number</div>
    </div>

    {#if responseNumber}
      <div class="stat">
        <div class="stat-title">Squared</div>
        <div class="stat-value text-primary">{responseNumber.square}</div>
        <div class="stat-desc">When you multiply a number by itself</div>
      </div>

      <div class="stat">
        <div class="stat-title">Divisors</div>
        <div class="stat-value text-primary">
          {responseNumber.divisors.map((d) => d.divisor).join(", ")}
        </div>
        <div class="stat-desc">
          {#if responseNumber.divisors.length === 2}
            {params.number} is a prime number
          {:else}
            All of this number's factors
          {/if}
        </div>
      </div>
    {/if}
  </div>

  <div class="mt-5">
    {#if !responseNumber}
      <button class="btn btn-sm btn-success" on:click={handleCreateNumber}
        >Calculate stats</button
      >
    {/if}
    <button class="btn btn-sm btn-success" on:click={handleRandomiseNumber}
      >Randomise</button
    >
  </div>
</div>
