<script>
  import { onMount } from "svelte";

  export let params;

  let responseNumber = null;

  $: params, fetchNumberDetails();
  async function fetchNumberDetails() {
    const res = await fetch(
      import.meta.env.VITE_API_BASE_URL + `/number/` + params.number
    );
    responseNumber = await res.json();
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

<p>
  Number: {params.number}
</p>

{#if responseNumber}
  <p>
    Squared: {responseNumber.square}
  </p>

  <p>
    Divisors: {responseNumber.divisors.map((d) => d.divisor).join(", ")}
  </p>
{:else}
  <p>Number not found in database. Would you like to create it?</p>

  <p>
    <button on:click={handleCreateNumber}>Create {params.number}</button>
  </p>
{/if}
